import numpy as np

from moleculetda.structure_to_vectorization import structure_to_pd


def test_regression_mof_tda(mof_path):
    """Regression test for the TDA calculation."""
    dgms = structure_to_pd(mof_path, supercell_size=10)
    assert isinstance(dgms, dict)
    assert len(dgms) == 4
    assert list(dgms.keys()) == ["dim0", "dim1", "dim2", "dim3"]
    assert isinstance(dgms["dim1"], np.ndarray)

    dgms = structure_to_pd(mof_path, supercell_size=10, periodic=True)
    assert isinstance(dgms, dict)
    assert len(dgms) == 4
    assert list(dgms.keys()) == ["dim0", "dim1", "dim2", "dim3"]
    assert isinstance(dgms["dim1"], np.ndarray)
