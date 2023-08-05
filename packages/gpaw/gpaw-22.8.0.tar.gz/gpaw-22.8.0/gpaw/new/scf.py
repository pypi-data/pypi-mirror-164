from __future__ import annotations

import itertools
import warnings
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

from gpaw.convergence_criteria import (Criterion, check_convergence,
                                       dict2criterion)
from gpaw.scf import write_iteration
from gpaw.yml import indent

if TYPE_CHECKING:
    from gpaw.new.calculation import DFTState


class SCFConvergenceError(Exception):
    ...


class SCFLoop:
    def __init__(self,
                 hamiltonian,
                 occ_calc,
                 eigensolver,
                 mixer,
                 world,
                 convergence,
                 maxiter):
        self.hamiltonian = hamiltonian
        self.eigensolver = eigensolver
        self.mixer = mixer
        self.occ_calc = occ_calc
        self.world = world
        self.convergence = convergence
        self.maxiter = maxiter
        self.niter = 0
        self.update_density_and_potential = True

    def __repr__(self):
        return 'SCFLoop(...)'

    def __str__(self):
        return (f'eigensolver:\n{indent(self.eigensolver)}\n'
                f'{self.mixer}\n'
                f'occupation numbers:\n{indent(self.occ_calc)}\n')

    def iterate(self,
                state: DFTState,
                pot_calc,
                convergence=None,
                maxiter=None,
                log=None):

        cc = create_convergence_criteria(convergence or self.convergence)
        maxiter = maxiter or self.maxiter

        if log:
            log('convergence criteria:')
            for criterion in cc.values():
                if criterion.description is not None:
                    log('- ' + criterion.description)
            log(f'maximum number of iterations: {self.maxiter}\n')

        self.mixer.reset()

        if self.update_density_and_potential:
            dens_error = self.mixer.mix(state.density)
        else:
            dens_error = 0.0

        for self.niter in itertools.count(start=1):
            wfs_error = self.eigensolver.iterate(state, self.hamiltonian)
            state.ibzwfs.calculate_occs(
                self.occ_calc,
                fixed_fermi_level=not self.update_density_and_potential)

            ctx = SCFContext(
                state, self.niter,
                wfs_error, dens_error,
                self.world)

            yield ctx

            converged, converged_items, entries = check_convergence(cc, ctx)
            if log:
                with log.comment():
                    write_iteration(cc, converged_items, entries, ctx, log)
            if converged:
                break
            if self.niter == maxiter:
                raise SCFConvergenceError

            if self.update_density_and_potential:
                state.density.update(pot_calc.nct_R, state.ibzwfs)
                dens_error = self.mixer.mix(state.density)
                state.potential, state.vHt_x, _ = pot_calc.calculate(
                    state.density, state.vHt_x)


class SCFContext:
    def __init__(self,
                 state: DFTState,
                 niter: int,
                 wfs_error: float,
                 dens_error: float,
                 world):
        self.state = state
        self.niter = niter
        energy = (sum(state.potential.energies.values()) +
                  sum(state.ibzwfs.energies.values()))
        self.ham = SimpleNamespace(e_total_extrapolated=energy)
        self.wfs = SimpleNamespace(nvalence=state.ibzwfs.nelectrons,
                                   world=world,
                                   eigensolver=SimpleNamespace(
                                       error=wfs_error),
                                   nspins=state.density.ndensities,
                                   collinear=state.density.collinear)
        self.dens = SimpleNamespace(
            calculate_magnetic_moments=state.density
            .calculate_magnetic_moments,
            fixed=False,
            error=dens_error)


def create_convergence_criteria(criteria: dict[str, Any]
                                ) -> dict[str, Criterion]:
    for k, v in [('energy', 0.0005),        # eV / electron
                 ('density', 1.0e-4),       # electrons / electron
                 ('eigenstates', 4.0e-8)]:  # eV^2 / electron
        if k not in criteria:
            criteria[k] = v
    # Gather convergence criteria for SCF loop.
    custom = criteria.pop('custom', [])
    for name, criterion in criteria.items():
        if hasattr(criterion, 'todict'):
            # 'Copy' so no two calculators share an instance.
            criteria[name] = dict2criterion(criterion.todict())
        else:
            criteria[name] = dict2criterion({name: criterion})

    if not isinstance(custom, (list, tuple)):
        custom = [custom]
    for criterion in custom:
        if isinstance(criterion, dict):  # from .gpw file
            msg = ('Custom convergence criterion "{:s}" encountered, '
                   'which GPAW does not know how to load. This '
                   'criterion is NOT enabled; you may want to manually'
                   ' set it.'.format(criterion['name']))
            warnings.warn(msg)
            continue

        criteria[criterion.name] = criterion
        msg = ('Custom convergence criterion {:s} encountered. '
               'Please be sure that each calculator is fed a '
               'unique instance of this criterion. '
               'Note that if you save the calculator instance to '
               'a .gpw file you may not be able to re-open it. '
               .format(criterion.name))
        warnings.warn(msg)

    for criterion in criteria.values():
        criterion.reset()

    return criteria
