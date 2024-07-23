'''
molecule
'''

from typing import Sequence
from .measure import calculate_distance

def build_bond_list(coordinates: Sequence[Sequence[float]], 
                    max_bond: float = 1.5, 
                    min_bond: float = 0) -> dict[tuple[int, int], float]:
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds