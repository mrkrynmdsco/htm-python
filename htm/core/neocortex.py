
from htm.core.sdr import SDR


class Synapse:
    """ HTM Synapse """

    def __init__(self):
        self._learn_rate = 0.01
        self._threshold = 0.2
        self._permanence = 0.0


class Dendrite:
    """ HTM Dendrite """

    def __init__(self):
        self._feed = None
        self._synapses = None


class Cell:
    """ HTM Cell """

    def __init__(self, idx: int):
        self._idx = None
        self._proximal = None
        self._apical = None
        self._distal_input = None
        self._distal_output = None

        self._state = 'inactive'  # [active, inactive, predicted]


class Grid:
    """ HTM Grid Cell """
    pass
