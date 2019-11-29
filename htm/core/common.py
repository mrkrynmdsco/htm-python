
from enum import Enum


class htmObj:
    """ HTM Object Class """

    def __init__(self, idx: int = 0):
        self._idx = None  # object index in a system

    # GETTER FUNCTIONS
    # ----------------
    @property
    def idx(self):
        return self._idx

    # SETTER FUNCTIONS
    # ----------------
    @idx.setter
    def idx(self, i: int):
        self._idx = i

    # METHODS
    # -------
    def update(self):
        raise NotImplementedError


class htmState(Enum):
    """ HTM Object States """
    INACTIVE = 0
    ACTIVE = 1
    PREDICTED = 2
