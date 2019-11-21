
import torch
import torch.cuda as cuda


def compute_nbits(n: int) -> int:
    return int(2 ** n)


def compute_population(n: int, s: float) -> int:
    return int(n * s)


class SparseDistributedRepresentation:
    """
    Sparse Distributed Representation

        The representation data format of HTM Systems
    ...

    Parameters
    ----------
    bitres: int
        - bit resolution of representation
    spct: float
        - ratio of active bitd to total number of bits in the vector
        - applicable range [0.005 : 0.02]

    Attributes
    ----------
    nbits : int
        - number of bits in the vector
    sparsity : float
        - sparse percentage
    wbits : int
        - number of active bits

    Methods
    -------

    """

    def __init__(self, bitres: int = 12, spct: float = 0.02):
        self._bitres = bitres
        self._spct = spct

        self._nbits = compute_nbits(self.bitres)
        self._wbits = compute_population(self.nbits, self.sparsity)

        if cuda.is_available():
            self._dense = cuda.BoolTensor(self.nbits)
            self._sparse = torch.zeros(self.wbits, dtype=torch.int32, device=torch.device('cuda:0'))
        else:
            self._dense = torch.BoolTensor(self.nbits)
            self._sparse = torch.zeros(self.wbits, dtype=torch.int32)

    @property
    def bitres(self):
        return self._bitres

    @bitres.setter
    def bitres(self, b: int):
        self._bitres = b
        compute_nbits(self.bitres)

    @property
    def sparsity(self):
        return self._spct

    @sparsity.setter
    def sparsity(self, s: float):
        self._spct = s

    @property
    def nbits(self):
        return self._nbits

    @property
    def wbits(self):
        return self._wbits

    @property
    def dense(self):
        return self._dense

    @property
    def sparse(self):
        return self._sparse

    @sparse.setter
    def sparse(self, t: torch.Tensor):
        if t.size() == self.sparse.size():
            self._sparse = t
        else:
            raise Exception('Tensor size mismatch. {} is expected.'.format(self.sparse.size()))

    def view_dense(self, row: int = 64, col: int = 64):
        if cuda.is_available():
            return self.dense.type(cuda.ByteTensor).view((row, col))
        else:
            return self.dense.type(torch.ByteTensor).view((row, col))

    def view_sparse(self, row: int = 9, col: int = 9):
        return self.sparse.view((row, col))


class SDR(SparseDistributedRepresentation):
    """Alias for SparseDistributedRepresentation Class"""
    pass
