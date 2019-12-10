
from htm.core.cortex import BaseHTM
from htm.core.cortex import (PREDICTED, INACTIVE, ACTIVE)


class Region:
    """ HTM Region """
    def __init__(self):
        self._columns = None

    def cols_sdr(self):
        pass


class Layer:
    """ HTM Layer """
    def __init__(self):
        pass


class HyperColumn (BaseHTM):
    """ HTM Hyper Column (macro-column) """
    def __init__(self):
        super().__init__()


class Network:
    """ HTM Network """

    def __init__(self):
        pass
