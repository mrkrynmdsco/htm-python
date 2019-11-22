
import torch
import torch.cuda as cuda
import numpy as np
import matplotlib.pyplot as plt


def compute_nbits(n: int) -> int:
    return int(2 ** n)


def compute_wbits(n: int, s: float) -> int:
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
    sprpct: float
        - ratio of active bits to total number of bits in the vector (sparse percentage)
        - suggested range [0.005 : 0.02]

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
    to_sdr()

    """

    def __init__(self, bitres: int = 12, sprpct: float = 0.02):
        self._bitres = bitres
        self._sprpct = sprpct
        self._device = 'cuda' if cuda.is_available() else 'cpu'

        self._nbits = compute_nbits(self.bitres)
        self._wbits = compute_wbits(self.nbits, self.sparsity)

        self._sparse = []  # a Tensor of indices of each ACTIVE bits
        self._coords = []  # a Tensor of coordinates of each ACTIVE bits

        self._dense = []  # Dense representation (read-only)

    @property
    def bitres(self):
        return self._bitres

    @bitres.setter
    def bitres(self, b: int):
        self._bitres = b
        self._nbits = compute_nbits(self.bitres)

    @property
    def sparsity(self):
        return self._sprpct

    @sparsity.setter
    def sparsity(self, s: float):
        self._sprpct = s
        self._wbits = compute_wbits(self.nbits, self.sparsity)

    @property
    def device(self):
        return self._device

    @property
    def nbits(self):
        return self._nbits

    @property
    def wbits(self):
        return self._wbits

    @property
    def sparse(self):
        return self._sparse

    @sparse.setter
    def sparse(self, idxs: [int]):
        if len(idxs) == self.wbits:
            self._sparse = torch.tensor(data=idxs, dtype=torch.int32, device=self.device)
            # TODO Update self.coords to reflect the change here!
        else:
            raise Exception('Element size mismatch. Size ({}) is expected. \
                ({}) provided'.format(self.wbits, len(idxs)))

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self):
        # TODO Implement this!
        raise NotImplementedError

    def dense(self, raw: bool = True):
        self._dense = torch.tensor([False] * self.nbits, dtype=torch.bool, device=self.device)

        if isinstance(self.sparse, cuda.IntTensor) or isinstance(self.sparse, torch.IntTensor):
            self._dense = self._dense.scatter_(0, self.sparse.type(torch.int64), True)
        else:
            pass

        if raw:
            return self._dense
        else:
            return self._dense.type(torch.ByteTensor)

    def view(self, form: str = 'dense', dims: tuple = (64, 64), figsize: tuple = (8, 8)):
        if 'dense' == form:
            sdr = self.dense(raw=False).view(dims)

        elif 'sparse' == form:
            sdr = self.sparse.view(dims)

        plt.figure(figsize=figsize)
        plt.imshow(sdr.numpy())
        plt.show()


class SDR(SparseDistributedRepresentation):
    """Alias for SparseDistributedRepresentation Class"""
    pass
