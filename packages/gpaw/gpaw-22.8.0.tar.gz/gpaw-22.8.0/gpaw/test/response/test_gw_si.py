"""Test GW band-gaps for Si."""

import pytest
from ase.build import bulk

from gpaw import GPAW, PW, FermiDirac
from gpaw.mpi import world
from gpaw.response.g0w0 import G0W0


def generate_si_systems():
    a = 5.43
    si1 = bulk('Si', 'diamond', a=a)
    si2 = si1.copy()
    si2.positions -= a / 8

    return [si1, si2]


def run(atoms, symm, nblocks):
    atoms.calc = GPAW(mode=PW(250),
                      eigensolver='rmm-diis',
                      occupations=FermiDirac(0.01),
                      symmetry=symm,
                      kpts={'size': (2, 2, 2), 'gamma': True},
                      convergence={'density': 1e-7},
                      parallel={'domain': 1},
                      txt='si.txt')
    e = atoms.get_potential_energy()
    scalapack = atoms.calc.wfs.bd.comm.size
    atoms.calc.diagonalize_full_hamiltonian(nbands=8, scalapack=scalapack)
    atoms.calc.write('si.gpw', mode='all')
    # The first iteration of the loop has very few frequencies.
    # The test is, that code should still not crash.
    # The second iteration is the actual numerical test, which
    # will be returned and asserted outside this function.
    for omegamax in [0.2, None]:
        gw = G0W0('si.gpw',
                  'gw',
                  nbands=8,
                  integrate_gamma=0,
                  kpts=[(0, 0, 0), (0.5, 0.5, 0)],  # Gamma, X
                  ecut=40,
                  nblocks=nblocks,
                  frequencies={'type': 'nonlinear',
                               'domega0': 0.1, 'omegamax': omegamax},
                  eta=0.2,
                  relbands=(-1, 2))
        results = gw.calculate()

    G, X = results['eps'][0]
    output = [e, G[0], G[1] - G[0], X[1] - G[0], X[2] - X[1]]
    G, X = results['qp'][0]
    output += [G[0], G[1] - G[0], X[1] - G[0], X[2] - X[1]]

    return output


reference = pytest.approx([-9.253, 5.442, 2.389, 0.403, 0.000,
                           6.261, 3.570, 1.323, 0.001], abs=0.003)


@pytest.mark.response
@pytest.mark.slow
@pytest.mark.parametrize('si', generate_si_systems())
@pytest.mark.parametrize('symm', [{},
                                  'off',
                                  {'time_reversal': False},
                                  {'point_group': False}])
@pytest.mark.parametrize('nblocks',
                         [x for x in [1, 2, 4, 8] if x <= world.size])
def test_response_gwsi(in_tmp_dir, si, symm, nblocks, scalapack):
    assert run(si, symm, nblocks) == reference


@pytest.mark.response
@pytest.mark.ci
@pytest.mark.parametrize('si', generate_si_systems())
@pytest.mark.parametrize('symm', [{}])
def test_small_response_gwsi(in_tmp_dir, si, symm, scalapack):
    assert run(si, symm, 1) == reference
