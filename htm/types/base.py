
class CorticalObject (object):
    def __init__(self):
        self._idx = None


class ObjectHTM (object):
    """ HTM Base Object """

    def __init__(self):
        self._cfg = {}

    def cfg(self, key: str):
        return self._cfg[key]

    def set_cfg(self, key: str, value):
        self._cfg[key] = value

    def get_configs(self):
        return self._cfg

    def set_configs(self, cfg: dict):
        self._cfg = cfg


class MemoryHTM (ObjectHTM):
    """ HTM Memory Object """

    def __init__(self):
        super().__init__()

        self._size = None
        self._pooler = None

        self._cells = None
        self._segments = None
        self._synapses = None

    def size(self):
        return self._size

    def pooler(self):
        return self._pooler

    def set_size(self, size):
        self._size = size

    def set_pooler(self, pooler):
        self._pooler = pooler

    def compute(self, input, learn, output):
        raise NotImplementedError
