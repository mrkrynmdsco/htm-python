
from htm.core.sdr import SDR


class Synapse:
    """ HTM Synapse """

    def __init__(self):
        self._permanence = None
        self._learn_rate = None
        self._state = None  # ['connected', 'unconnected', 'potential']


class Segment:
    """ HTM Segment """

    def __init__(self):
        self._feed = None
        self._synapses = None


class Cell:
    """ HTM Cell """

    def __init__(self):
        self._apical = Segment()  # apical segments (feed-back)
        self._distal = Segment()  # distal segments (context feed)
        self._proximal = Segment()  # proximal segments (feed-forward)

        self._state = 'inactive'  # ['active', 'inactive', 'predicted']


class Grid:
    """ HTM Grid Cell """
    pass
