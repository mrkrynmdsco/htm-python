
from htm.types.base import CorticalObject


class Synapse (CorticalObject):
    def __init__(self):
        super().__init__()
        self._permanence = None
        self._presynaptic_cell = None


class Segment (CorticalObject):
    def __init__(self):
        super().__init__()
        self._synapses = None
        self._cell_idx = None


class Cell (CorticalObject):
    def __init__(self):
        super().__init__()
        self._segments = None
