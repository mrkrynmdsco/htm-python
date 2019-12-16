
from htm.types.base import CorticalObject


class Synapse (CorticalObject):
    def __init__(self):
        super().__init__()
        self._permanence = None
        self._presyncell = None


class Segment (CorticalObject):
    def __init__(self):
        super().__init__()
        self._mothercell = None
        self._synapses = None


class Cell (CorticalObject):
    def __init__(self):
        super().__init__()
        self._segments = None
        self._mothercolumn = None
