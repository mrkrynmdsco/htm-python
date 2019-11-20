
import torch
import torch.cuda as cuda


class SparseDistributedRepresentation:
    """
    Sparse Distributed Representation

    ...

    Parameter
    ---------
    resolution: int
        bit resolution
    sparsity: float
        ratio of active cells to total number of cells

    Attributes
    ----------
    ncells : int
        number of cells
    sparsity : float
        sparse percentage
    wcells : int
        number of active cells

    Methods
    -------

    """

    def __init__(self, resolution: int = 12, sparsity: float = 0.02):
        self._resolution = resolution
        self._sparsity = sparsity

        self._ncells = int(2 ** self.resolution)
        self._wcells = self._compute_population(self.ncells, self.sparsity)

        if cuda.is_available():
            self._dense = cuda.BoolTensor(self.ncells)
        else:
            self._dense = torch.BoolTensor(self.ncells)

        self._sparse = torch.zeros(self.wcells, dtype=torch.int32)

    @property
    def resolution(self):
        return self._resolution

    @property
    def sparsity(self):
        return self._sparsity

    @property
    def ncells(self):
        return self._ncells

    @property
    def wcells(self):
        return self._wcells

    @property
    def dense(self):
        return self._dense

    @property
    def sparse(self):
        return self._sparse

    @staticmethod
    def _compute_population(n: int, s: float) -> int:
        return int(n * s)


class SDR(SparseDistributedRepresentation):
    """Alias for SparseDistributedRepresentation Class"""
    pass
