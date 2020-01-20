
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
        if sort:
            self._indxs = np.sort(rng.choice(a=np.arange(0, self.nbits), size=self.wbits, replace=False))
        else:
            self._indxs = rng.choice(a=np.arange(0, self.nbits), size=self.wbits, replace=False)

    def dense(self, shape: tuple = None):
        d = np.zeros(self.nbits, dtype=np.bool)
        np.put_along_axis(arr=d, indices=self.sparse(), values=True, axis=None)

        if shape:
            return d.reshape(shape)
        else:
            return d

    def info(self):
        print('size: {}'.format(self.nbits))
        print('on-bits: {}'.format(self.wbits))
        print('sparsity: {:0.3f} %'.format(self.sparsity * 100))

    def show(self, shape: tuple, figsize: tuple = (8, 8)):
        d = self.dense(shape)
        plt.figure(figsize=figsize)
        plt.imshow(d, cmap='cividis')
        plt.show()


class SDRMetrics:
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
