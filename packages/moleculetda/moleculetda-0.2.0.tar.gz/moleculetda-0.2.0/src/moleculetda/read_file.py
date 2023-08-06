"""
Read the appropriate file type and transform accordingly to point cloud data.
"""
from pathlib import Path
from typing import Tuple, Union

import numpy as np
from loguru import logger
from pymatgen.core import Molecule, Structure
from pymatgen.transformations.advanced_transformations import CubicSupercellTransformation


def read_data(
    filename: Union[str, Path],
    size: Union[Tuple[int], None] = None,
    supercell: bool = False,
    periodic: bool = False,
) -> np.ndarray:
    """
    Args:
        filename (str, Path): currently supports cif, .npy
        size (Tuple[int], None): if creating a cubic supercell, size of the cell. Defaults to None
        supercell (bool): if creating a supercell, only supported by ".cif" option for now
        periodic (bool): if creating a periodic supercell, only supported by ".cif" option for now
    """
    filename = Path(filename)
    if filename.suffix == ".cif":
        if supercell:
            lattice_matrix, xyz = read_cif(filename)
            if periodic:
                s = Structure.from_file(filename)
                supercell_structure = CubicSupercellTransformation(
                    min_length=size
                ).apply_transformation(s)
                return supercell_structure.frac_coords
            return make_supercell(xyz, lattice_matrix, size)
        else:
            return read_cif(filename)[1]  # xyz coordinates
    elif filename.suffix == ".npy":
        return np.load(filename)
    else:
        raise NotImplementedError("Other file types not implemented.")


def read_cif(filename: Union[str, Path]) -> Tuple[np.ndarray, np.ndarray]:

    structure = Structure.from_file(filename)

    lattice_matrix = structure.lattice.matrix
    xyz = structure.cart_coords
    return (lattice_matrix, xyz)


def make_supercell(
    coords: np.ndarray, lattice: Tuple[float, float, float], size: float, min_size: float = -5
) -> np.ndarray:
    """
    Generate cubic supercell of a given size.

    Args:
        coords (np.ndarray): matrix of xyz coordinates of the system
        lattice (Tuple[float, float, float]): lattice constants of the system
        size (float): dimension size of cubic cell, e.g., 10x10x10
        min_size (float): minimum axes size to keep negative xyz coordinates from the original cell

    Returns:
        new_cell: supercell array
    """
    a, b, c = lattice

    xyz_periodic_copies = []
    xyz_periodic_copies.append(coords)
    min_range = -3  # we aren't going in the minimum direction too much, so can make this small
    max_range = 20  # make this large enough, but can modify if wanting an even larger cell

    for x in range(-min_range, max_range):
        for y in range(0, max_range):
            for z in range(0, max_range):
                if x == y == z == 0:
                    continue
                add_vector = x * a + y * b + z * c
                xyz_periodic_copies.append(coords + add_vector)

    # Combine into one array
    xyz_periodic_total = np.vstack(xyz_periodic_copies)

    # Filter out all atoms outside of the cubic box
    new_cell = xyz_periodic_total[np.max(xyz_periodic_total[:, :3], axis=1) < size]
    new_cell = new_cell[np.min(new_cell[:, :3], axis=1) > min_size]

    return new_cell
