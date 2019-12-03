
from enum import Enum


class htmState (Enum):
    """ HTM Object States """
    pass


class SynapseState (htmState):
    """ HTM Synapse States """
    UNCONNECTED = 0
    CONNECTED = 1


class DendriteState (htmState):
    """ HTM Dendrite States """
    OFF = 0
    ON = 1


class CellState (htmState):
    """ HTM Cell States """
    INACTIVE = 0
    ACTIVE = 1
    PREDICTED = 2


class htmObj:
    """ HTM Object Class """

    def __init__(self, idx: int = 0):
        self._idx = None  # object index in a system
        self._state = None  # object state
        self._thres = None  # object activation threshold

    # GETTER FUNCTIONS
    # ----------------
    @property
    def idx(self):
        return self._idx

    @property
    def state(self):
        return self._state

    @property
    def activation_threshold(self):
        return self._thres

    # SETTER FUNCTIONS
    # ----------------
    @idx.setter
    def idx(self, i: int):
        self._idx = i

    @state.setter
    def state(self, s):
        self._state = s

    @activation_threshold.setter
    def activation_threshold(self, t):
        self._thres = t

    # METHODS
    # -------
    def update(self):
        raise NotImplementedError
