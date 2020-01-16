
import numpy as np
import matplotlib.pyplot as plt


class SDR:
    """ Sparse Distributed Representation (htm) """

    def __init__(self):
        self._nbits = None  # vector size
        self._sprct = None  # sparsity
        self._wbits = None  # vector cardinality

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
