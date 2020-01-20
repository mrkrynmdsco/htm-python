
import numpy as np
import matplotlib.pyplot as plt


class SDR:
    """ Sparse Distributed Representation (htm) """

    def __init__(self, n: int, s: float):
        self._nbits = n             # vector size
        self._sprct = s             # sparsity (percentage)
        self._wbits = round(n * s)  # vector cardinality

        self._indxs = None

    @property
    def nbits(self):
        return self._nbits

    @property
    def wbits(self):
        return self._wbits

    @property
    def sparsity(self):
        return self._sprct

    def sparse(self):
        return self._indxs

    def set_sparse(self, idxs: list):
        if len(idxs) == self.wbits:
            self._indxs = np.array(idxs)
        else:
            raise Exception('Invalid vector size!')

    def random_sparse(self, seed: int = 666, sort: bool = True):
        rng = np.random.default_rng(seed=seed)
        self._indxs = rng.choice(a=np.arange(0, self.nbits), size=self.wbits, replace=False)
        if sort:
            self._indxs = np.sort(self._indxs)

    def dense(self, shape: tuple = None):
        d = np.zeros(self.nbits, dtype=np.bool)
        np.put_along_axis(arr=d, indices=self.sparse(), values=True, axis=None)

        if shape:
            return d.reshape(shape)
        else:
            return d

    def show(self, shape: tuple, figsize: tuple = (8, 8), cmap='cividis'):
        d = self.dense(shape)

        print('Dense Representation (re-shaped)')
        print('dtype: {}'.format(d.dtype))
        print('ndim: {}'.format(d.ndim))
        print('strides: {}'.format(d.strides))
        print('shape: {}'.format(d.shape))
        print('size: {}'.format(d.size))
        print('data: {}'.format(d.data))

        plt.figure(figsize=figsize)
        plt.imshow(d, cmap=cmap)
        plt.show()

    def info(self):
        print('Sparse Distributed Representation')
        print('size: {}'.format(self.nbits))
        print('on-bits: {}'.format(self.wbits))
        print('sparsity: {:0.3f} %'.format(self.sparsity * 100))


class Metrics:
    """ SDR Metrics (htm) """

    def capacity(self, x: SDR):
        pass

    def overlap(self, x: SDR, y: SDR):
        pass

    def match(self, x: SDR, y: SDR):
        pass

    def sample(self):
        pass

    def union(self):
        pass
