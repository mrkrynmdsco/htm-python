
import numpy as np


class SparseDistributedRepresentation:
    """
    Sparse Distributed Representation

    ...

    Attributes
    ----------
    ncells : int
        number of cells
    sparsity : float
        sparse percentage
    wcells : int
        number of active cells

    """

    def __init__(self, ncells: int = 2048, sparsity: float = 0.02):
        self._ncells = ncells
        self._sparsity = sparsity
        self._wcells = self._compute_population(ncells, sparsity)

        self._dense = None
        self._sparse = None

    @property
    def ncells(self):
        return self._ncells

    @property
    def sparsity(self):
        return self._sparsity

    @property
    def wcells(self):
        return self._wcells

    @staticmethod
    def _compute_population(n: int, s: float) -> int:
        return int(n * s)


class SDR(SparseDistributedRepresentation):
    """Alias for SparseDistributedRepresentation Class"""
    pass
