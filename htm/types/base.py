
from htm.types.state import StateHTM


class BaseHTM (object):
    """ HTM Base Object """

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


class MemoryHTM (object):
    """ HTM Memory """

    def __init__(self):
        self._size = None
        self._pooler = None
        self._cfg = {}

    def size(self):
        return self._size

    def pooler(self):
        return self._pooler

    def cfg(self, key):
        return self._cfg[key]

    def set_size(self, size):
        self._size = size

    def set_pooler(self, pooler):
        self._pooler = pooler

    def set_cfg(self, key, value):
        self._cfg[key] = value

    def compute(self, input, learn, output):
        raise NotImplementedError
