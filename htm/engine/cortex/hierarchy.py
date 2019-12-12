
from htm.core.cortex import BaseHTM
from htm.core.memory import (InputMemory, SpatialMemory, TemporalMemory)
from htm.core.cortex import (PREDICTED, INACTIVE, ACTIVE)


class Region (BaseHTM):
    """ HTM Region """
    def __init__(self):
        super().__init__()
        self._cfg = {
            'input_dims': [32, 32],
            'column_dims': [64, 64],
        }
        self._imem = None
        self._smem = None
        self._tmem = None

    def columns_sdr(self):
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
