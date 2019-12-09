
import random
from enum import Enum


class StateHTM (Enum):
    PREDICTED = -1
    INACTIVE = False
    ACTIVE = True


PREDICTED = StateHTM.PREDICTED
INACTIVE = StateHTM.INACTIVE
ACTIVE = StateHTM.ACTIVE


class BaseHTM:
    def __init__(self):
        self._index = None
        self._state = None
        self._cfg = {}

    def get_index(self):
        return self._index

    def get_state(self):
        return self._state

    def get_config(self, key):
        return self._cfg[key]

    def get_configs(self):
        return self._cfg

    def set_index(self, i: int):
        self._index = i

    def set_state(self, s: StateHTM):
        self._state = s

    def set_config(self, key, value):
        self._cfg[key] = value

    def set_configs(self, cfg: dict):
        self._cfg = cfg

    def update(self):
        raise NotImplementedError
