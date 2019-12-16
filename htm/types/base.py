
class CorticalObject (object):
    def __init__(self):
        self._idx = None
        self._state = None

    @property
    def idx(self):
        return self._idx

    @property
    def state(self):
        return self._state

    @idx.setter
    def idx(self, idx: int):
        self._idx = idx

    @state.setter
    def state(self, s):
        self._state = s


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

    def append_configs(self, cfg: dict):
        for key, value in cfg.items():
            self.set_cfg(key, value)


class MemoryHTM (ObjectHTM):
    """ HTM Memory Object """

    def __init__(self):
        super().__init__()
        cfg = {
            'shape': None,  # memory shape
            'ncols': None,  # memory number of columns
            'ncels': None,  # memory number of cells per column
        }
        self.set_configs(cfg)

        self._colmap = None     # column activation map
        self._celmap = None     # cell activation map
        self._conmap = None     # connection state map
        self._prdmap = None     # cell prediction map

    def get_shape(self):
        return self._cfg['shape']

    def get_ncolumns(self):
        return self._cfg['ncols']

    def get_ncells(self):
        return self._cfg['ncels']

    def set_shape(self, r: int, c: int):
        self._cfg['shape'] = (r, c)
        self._cfg['ncols'] = r * c

    def set_ncells(self, n: int):
        self._cfg['ncels'] = n

    def initialize(self):
        raise NotImplementedError

    def compute(self, input, outpur, islearn):
        raise NotImplementedError

    def render(self, mtype):
        raise NotImplementedError
