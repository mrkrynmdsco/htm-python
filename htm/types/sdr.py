
import numpy as np
import matplotlib.pyplot as plt


class SDR:
    """ Sparse Distributed Representation (htm) """

    def __init__(self, n: int, s: float):
        self._nbits = n             # vector size
        self._sprct = s             # sparsity (percentage)
        self._wbits = round(n * s)  # vector cardinality

    def dense(self):
        pass

    def sparse(self):
        pass


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
