
from htm.core.sdr import SDR


class Synapse:
    """ Learned Connection """

    def __init__(self):
        self._state = None  # ['connected', 'unconnected', 'potential']
        self._permanence = None


class Segment:
    """ Dendritic Segment """

    def __init__(self):
        self._synapses = None


class Cell:
    """ Neuron Cell """

    def __init__(self):
        self._apical = None  # apical segments (feedback)
        self._distal = None  # distal segments (contextual)
        self._proximal = None  # proximal segments (feedforward)

        self._state = None  # ['active', 'inactive', 'predicted']


class Grid:
    """ Grid Cell """
    pass
