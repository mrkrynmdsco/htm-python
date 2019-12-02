
from enum import Enum


class htmState(Enum):
    """ HTM Object States """
    INACTIVE = 0
    ACTIVE = 1
    PREDICTED = 2


class htmObj:
    """ HTM Object Class """

    def __init__(self, idx: int = 0):
        self._idx = None  # object index in a system
        self._state = None  # object state

    # GETTER FUNCTIONS
    # ----------------
    @property
    def idx(self):
        return self._idx

    @property
    def state(self):
        return self._state

    # SETTER FUNCTIONS
    # ----------------
    @idx.setter
    def idx(self, i: int):
        self._idx = i

    @state.setter
    def state(self, s: htmState):
        self._state = s

    # METHODS
    # -------
    def update(self):
        raise NotImplementedError
