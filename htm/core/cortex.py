
from enum import Enum


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

    def set_state(self, s):
        raise NotImplementedError

    def set_config(self, key, value):
        self._cfg[key] = value

    def set_configs(self, cfg: dict):
        self._cfg = cfg


class StateHTM (Enum):
    PREDICTED = -1
    INACTIVE = False
    ACTIVE = True


class Synapse (BaseHTM):
    """ HTM Synapse """
    def __init__(self):
        super().__init__()
        self._cfg = {
            'learn_rate': 0.003,
            'connect_threshold': 0.3,
            'min_permanence': 0.0,
            'max_permanence': 1.0,
        }
        self._srcid = None
        self._state = StateHTM.INACTIVE

        self._isconn = False
        self._permanence = 0.0

    def isconnected(self):
        return self._isconn

    def get_source_index(self):
        return self._srcid

    def get_permanence(self):
        return self._permanence

    def set_source_index(self, idx: int):
        self._srcid = idx

    def set_state(self, s: bool):
        self._state = s

    def set_permanence(self, p: float):
        MIN_P = self.get_config('min_permanence')
        MAX_P = self.get_config('max_permanence')

        if MIN_P <= p <= MAX_P:
            self._permanence = p
        elif MIN_P > p:
            self._permanence = MIN_P
        elif MAX_P < p:
            self._permanence = MAX_P
        else:
            raise Exception('Invalid permanence value being set: {}'.format(p))

    def _update_connection(self):
        p = self.get_permanence()
        t = self.get_config('connect_threshold')

        if t <= p:
            self._isconn = True
        else:
            self._isconn = False

    def increase_permanence(self):
        p = self.get_permanence()
        p = round(p + self.get_config('learn_rate'), 9)
        self.set_permanence(p)
        self._update_connection()

    def decrease_permanence(self):
        p = self.get_permanence()
        p = round(p - self.get_config('learn_rate'), 9)
        self.set_permanence(p)
        self._update_connection()


class Dendrite (BaseHTM):
    """ HTM Dendrite """
    def __init__(self):
        super().__init__()

        self._synapses = None


class Cell (BaseHTM):
    """ HTM Cell """
    def __init__(self):
        super().__init__()

        self._proximal = None
        self._distals = None
