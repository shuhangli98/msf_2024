import msf_2024
import numpy as np

import pytest


@pytest.fixture
def methane_molecule():
    # Static objects made once and shared on demand in tests.
    coordinates = np.array([[1.0, 1.0, 1.0], [2.4, 1.0, 1.0], [-0.4, 1.0, 1.0], [1.0, 1.0, 2.4], [1.0, 1.0, -0.4]])
    return coordinates


@pytest.fixture
def distance(methane_molecule):
    from scipy.spatial.distance import cdist
    coordinates = methane_molecule
    distances = cdist(coordinates, coordinates)
    return distances


def test_build_bond_list(methane_molecule):
    bond = msf_2024.build_bond_list(methane_molecule)
    assert len(bond) == 4
    for bond_length in bond.values():
        assert bond_length == 1.4


def test_fail_build_bond_list(methane_molecule):
    coordinates = np.array([[1.0, 1.0, 1.0], [2.4, 1.0, 1.0], [-0.4, 1.0, 1.0], [1.0, 1.0, 2.4], [1.0, 1.0, -0.4]])

    with pytest.raises(ValueError):
        msf_2024.build_bond_list(methane_molecule, min_bond=-1)


@pytest.mark.parametrize("max_bond", np.linspace(1, 5, num=4))
@pytest.mark.parametrize("min_bond", np.linspace(0, 0.5, num=4))
# This is a parametrized test. It will run 4*4 = 16 tests.
def test_build_bond_combine(methane_molecule, distance, max_bond, min_bond):
    coordinates = methane_molecule
    bonds = msf_2024.build_bond_list(coordinates, max_bond=max_bond, min_bond=min_bond)
    # will complete this function later.
