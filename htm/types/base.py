
import numpy as np


class _htmObj_ (object):
    """ HTM Base Object """

    def __init__(self):
        self._cfg = {}
        # self._device = 'cuda' if cuda.is_available() else 'cpu'

    def getcfg(self, key: str):
        return self._cfg[key]

    def setcfg(self, key: str, value):
        self._cfg[key] = value

    def getcfgs(self):
        return self._cfg

    def setcfgs(self, cfgs: dict):
        self._cfg = cfgs

    def append_cfgs(self, cfgs: dict):
        for key, value in cfgs.items():
            self.setcfg(key, value)


class Map (_htmObj_):
    """ Map (htm) """

    def __init__(self, size: int):
        super().__init__()
        cfg = {
            'size': size
        }
        self.setcfgs(cfg)
        self._map = None

    @property
    def size(self):
        return self.getcfg('size')

    @property
    def map(self):
        return self._map

    def initialize(self):
        raise NotImplementedError


class Memory (_htmObj_):
    """ Memory (htm) """

    def __init__(self):
        super().__init__()
        cfg = {
            'shape': None,
            'size': None,
        }
        self.setcfgs(cfg)
        self._mem = None

    @property
    def shape(self):
        return self.getcfg('shape')

    @property
    def size(self):
        return self.getcfg('size')

    @property
    def memory(self):
        return self._mem

    @shape.setter
    def shape(self, s: tuple):
        if 3 == len(s):  # 3D
            size = s[0] * s[1] * s[2]
        elif 2 == len(s):  # 2D
            size = s[0] * s[1] * 1
        else:
            raise Exception('Invalid memory shape!')

        self.setcfg('shape', s)
        self.setcfg('size', size)

    def initialize(self):
        self._mem = np.zeros(self.shape, dtype=bool)

    def configure(self):
        pass

    def read_input(self, input):
        pass

    def process(self):
        pass
