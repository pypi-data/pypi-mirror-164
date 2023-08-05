import numpy as np

import gpaw.mpi as mpi
from gpaw.response.susceptibility import (FourComponentSusceptibilityTensor,
                                          invert_dyson_single_frequency)

FCST = FourComponentSusceptibilityTensor


class TransverseMagneticSusceptibility(FCST):
    """Class calculating the transverse magnetic susceptibility
    and related physical quantities."""

    def __init__(self, *args, **kwargs):
        assert kwargs['fxc'] == 'ALDA'

        # Enable scaling to fit to Goldstone theorem
        if 'fxckwargs' in kwargs and 'fxc_scaling' in kwargs['fxckwargs']:
            self.fxc_scaling = kwargs['fxckwargs']['fxc_scaling']
        else:
            self.fxc_scaling = None

        FCST.__init__(self, *args, **kwargs)

    def get_macroscopic_component(self, spincomponent, q_c, frequencies,
                                  filename=None, txt=None):
        """Calculates the spatially averaged (macroscopic) component of the
        transverse magnetic susceptibility and writes it to a file.

        Parameters
        ----------
        spincomponent : str
            '+-': calculate chi+-, '-+: calculate chi-+
        q_c, frequencies, filename, txt : see gpaw.response.susceptibility

        Returns
        -------
        see gpaw.response.susceptibility
        """
        assert spincomponent in ['+-', '-+']

        return FCST.get_macroscopic_component(self, spincomponent, q_c,
                                              frequencies, filename=filename,
                                              txt=txt)

    def get_component_array(self, spincomponent, q_c, frequencies,
                            array_ecut=50, filename=None, txt=None):
        """Calculates a specific spin component of the
        transverse magnetic susceptibility and writes it to a file.

        Parameters
        ----------
        spincomponent : str
            '+-': calculate chi+-, '-+: calculate chi-+
        q_c, frequencies,
        array_ecut, filename, txt : see gpaw.response.susceptibility

        Returns
        -------
        see gpaw.response.susceptibility
        """
        assert spincomponent in ['+-', '-+']

        return FCST.get_component_array(self, spincomponent, q_c,
                                        frequencies, array_ecut=array_ecut,
                                        filename=filename, txt=txt)

    def get_xc_kernel(self, spincomponent, pd, chiks_wGG=None):
        """Get the exchange correlation kernel."""
        Kxc_GG = self.fxc(spincomponent, pd, txt=self.cfd)

        fxc_scaling = self.fxc_scaling

        if fxc_scaling is not None:
            assert isinstance(fxc_scaling[0], bool)
            if fxc_scaling[0]:
                if fxc_scaling[1] is None:
                    assert pd.kd.gamma
                    print('Finding rescaling of kernel to fulfill the '
                          'Goldstone theorem', file=self.fd)
                    mode = fxc_scaling[2]
                    assert mode in ['fm', 'afm']
                    omega_w = self.chiks.wd.omega_w
                    fxc_scaling[1] = get_goldstone_scaling(mode, omega_w,
                                                           chiks_wGG, Kxc_GG,
                                                           world=self.world)

                assert isinstance(fxc_scaling[1], float)
                Kxc_GG *= fxc_scaling[1]

        self.fxc_scaling = fxc_scaling

        return Kxc_GG


def get_goldstone_scaling(mode, omega_w, chiks_wGG, Kxc_GG, world=mpi.world):
    """Get kernel scaling parameter fulfilling the Goldstone theorem."""
    # Find the frequency to determine the scaling from
    wgs = find_goldstone_frequency(mode, omega_w)

    # Only one rank, rgs, has the given frequency and finds the rescaling
    nw = len(omega_w)
    mynw = (nw + world.size - 1) // world.size
    rgs, mywgs = wgs // mynw, wgs % mynw
    fxcsbuf = np.empty(1, dtype=float)
    if world.rank == rgs:
        chiks_GG = chiks_wGG[mywgs]
        fxcsbuf[:] = find_goldstone_scaling(mode, chiks_GG, Kxc_GG)

    # Broadcast found rescaling
    world.broadcast(fxcsbuf, rgs)
    fxcs = fxcsbuf[0]

    return fxcs


def find_goldstone_frequency(mode, omega_w):
    """Factory function for finding the appropriate frequency to determine
    the kernel scaling from according to different Goldstone criteria."""
    if mode == 'fm':
        return find_fm_goldstone_frequency(omega_w)
    elif mode == 'afm':
        return find_afm_goldstone_frequency(omega_w)
    else:
        raise ValueError(
            f"Allowed Goldstone scaling modes are 'fm', 'afm'. Got: {mode}")


def find_fm_goldstone_frequency(omega_w):
    """Find omega=0. as the fm Goldstone frequency."""
    wgs = np.abs(omega_w).argmin()
    if not np.allclose(omega_w[wgs], 0., atol=1.e-8):
        raise ValueError("Frequency grid needs to include"
                         + " omega=0. to allow 'fm' Goldstone scaling")

    return wgs


def find_afm_goldstone_frequency(omega_w):
    """Find the second smallest positive frequency
    as the afm Goldstone frequency."""
    # Set omega=0. and negative frequencies to np.inf
    omega1_w = np.where(omega_w < 1.e-8, np.inf, omega_w)
    # Sort for the two smallest positive frequencies
    omega2_w = np.partition(omega1_w, 1)
    # Find original index of second smallest positive frequency
    wgs = np.abs(omega_w - omega2_w[1]).argmin()

    return wgs


def find_goldstone_scaling(mode, chiks_GG, Kxc_GG):
    """Factory function for finding the scaling of the kernel
    according to different Goldstone criteria."""
    assert mode in ['fm', 'afm'],\
        f"Allowed Goldstone scaling modes are 'fm', 'afm'. Got: {mode}"

    if mode == 'fm':
        return find_fm_goldstone_scaling(chiks_GG, Kxc_GG)
    elif mode == 'afm':
        return find_afm_goldstone_scaling(chiks_GG, Kxc_GG)


def find_fm_goldstone_scaling(chiks_GG, Kxc_GG):
    """Find goldstone scaling of the kernel by ensuring that the
    macroscopic inverse enhancement function has a root in (q=0, omega=0)."""
    fxcs = 1.
    kappaM = calculate_macroscopic_kappa(chiks_GG, Kxc_GG * fxcs)
    # If kappaM > 0, increase scaling (recall: kappaM ~ 1 - Kxc Re{chi_0})
    scaling_incr = 0.1 * np.sign(kappaM)
    while abs(kappaM) > 1.e-7 and abs(scaling_incr) > 1.e-7:
        fxcs += scaling_incr
        if fxcs <= 0.0 or fxcs >= 10.:
            raise Exception('Found an invalid fxc_scaling of %.4f' % fxcs)

        kappaM = calculate_macroscopic_kappa(chiks_GG, Kxc_GG * fxcs)

        # If kappaM changes sign, change sign and refine increment
        if np.sign(kappaM) != np.sign(scaling_incr):
            scaling_incr *= -0.2

    return fxcs


def find_afm_goldstone_scaling(chiks_GG, Kxc_GG):
    """Find goldstone scaling of the kernel by ensuring that the
    macroscopic magnon spectrum vanishes at q=0. for finite frequencies."""
    fxcs = 1.
    SM = calculate_macroscopic_spectrum(chiks_GG, Kxc_GG * fxcs)
    # If SM > 0., increase the scaling. If SM < 0., decrease the scaling.
    scaling_incr = 0.1 * np.sign(SM)
    while (SM < 0. or SM > 1.e-7) or abs(scaling_incr) > 1.e-7:
        fxcs += scaling_incr
        if fxcs <= 0. or fxcs >= 10.:
            raise Exception('Found an invalid fxc_scaling of %.4f' % fxcs)

        SM = calculate_macroscopic_spectrum(chiks_GG, Kxc_GG * fxcs)

        # If chi changes sign, change sign and refine increment
        if np.sign(SM) != np.sign(scaling_incr):
            scaling_incr *= -0.2

    return fxcs


def calculate_macroscopic_kappa(chiks_GG, Kxc_GG):
    """Invert dyson equation and calculate the inverse enhancement function."""
    chi_GG = invert_dyson_single_frequency(chiks_GG, Kxc_GG)

    return (chiks_GG[0, 0] / chi_GG[0, 0]).real


def calculate_macroscopic_spectrum(chiks_GG, Kxc_GG):
    """Invert dyson equation and extract the macroscopic spectrum."""
    chi_GG = invert_dyson_single_frequency(chiks_GG, Kxc_GG)

    return - chi_GG[0, 0].imag / np.pi
