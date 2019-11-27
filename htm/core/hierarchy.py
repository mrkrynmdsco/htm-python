
from htm.core.neocortex import Cell
from htm.core.memory import InputMemory
from htm.core.memory import SpatialMemory
from htm.core.memory import TemporalMemory


class Column:
    """ HTM Column """

    def __init__(self):
        self._ncells = None

        self._is_active = False
        self._is_burst = False

        self._potential_rad = None
        self._potential_pct = None


class Region:
    """ HTM Region """

    def __init__(self):
        self._input_mem = InputMemory()  # Distributed to columns
        self._spatial_mem = SpatialMemory()  # Column level
        self._temporal_mem = TemporalMemory()  # Cell level


class Network:
    """ HTM Network """

    def __init__(self):
        pass
