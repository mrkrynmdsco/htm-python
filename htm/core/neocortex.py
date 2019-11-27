
from htm.core.sdr import SDR


class Synapse:
    """ HTM Synapse """

    def __init__(self):
        self._permanence = 0.0
        self._learn_rate = 0.05
        self._threshold = 0.5
        self._is_connected = False

    def update(self):
        if self._threshold <= self._permanence:
            self._is_connected = True

            if 1.0 < self._permanence:
                self._permanence = 1.0

        elif self._threshold > self._permanence:
            self._is_connected = False

            if 0.0 > self._permanence:
                self._permanence = 0.0

        else:
            self._is_connected = False

    def increment(self):
        self._permanence = self._permanence + self._learn_rate
        self.update()

    def decrement(self):
        self._permanence = self._permanence - self._learn_rate
        self.update()


class Segment:
    """ HTM Segment """

    def __init__(self, nsyns: int, feed: SDR):
        self._synapses = [Synapse] * nsyns  # [potential and functional synapses]
        self._feed = feed


class Cell:
    """ HTM Cell """

    def __init__(self):
        self._apical = []  # apical segments (feed-back)
        self._distal = []  # distal segments (context feed)
        self._proximal = [None]  # proximal segments (feed-forward)

        self._state = 'inactive'  # ['active', 'inactive', 'predicted']

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s: str):
        if s in ['active', 'inactive', 'predicted']:
            self._state = s
        else:
            raise Exception('Invalid cell state.')

    def set_segment(self, segment: Segment, segtype: str):
        if 'proximal' == segtype:
            self._proximal[0] = segment  # only one (1) segment allowed

        elif 'distal' == segtype:
            self._distal.append(segment)

        elif 'apical' == segtype:
            self._apical.append(segment)

        else:
            raise Exception('Invalid segment type.')


class Grid:
    """ HTM Grid Cell """
    pass
