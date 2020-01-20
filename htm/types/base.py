
import numpy as np


class _htmObj_:
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

        self._ffimap = None     # feed-forward input map
        self._fbimap = None     # feed-backward input map
        self._conmap = None     # cells connections map
        self._permap = None     # synapses permanence map

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
        tl = len(s)
        if tl == 3:  # 3D
            size = s[0] * s[1] * s[2]
        elif tl == 2:  # 2D
            size = s[0] * s[1] * 1
        else:
            raise Exception('Invalid memory shape!')

        self.setcfg('shape', s)
        self.setcfg('size', size)

    def initialize(self):
        self._mem = np.zeros(self.shape, dtype=np.bool)

    def configure(self):
        pass

    def read(self):
        pass

    def load(self):
        pass

    def process(self):
        pass

    def save(self):
        pass


class MemoryHTM (_htmObj_):
    """ HTM Memory Object """

    def __init__(self):
        super().__init__()
        cfg = {
            'ncols': None,      # memory number of columns
            'ncels': None,      # memory number of cells per column
            'nsegs': None,      # memory number of segments per cell
            'nsyns': None,      # memory number of synapses per segment

            'max_ncols': None,  # maximum number of columns
            'max_ncels': None,  # maximum number of cells per column
            'max_nsegs': None,  # maximum number of segments per cell
            'max_nsyns': None,  # maximum number of synapses per segment
        }
        self.setcfgs(cfg)

        self._colmap = None     # columns activation map
        self._celmap = None     # cells activation map
        self._segmap = None     # segments activation map
        self._synmap = None     # synapses activation map
        self._conmap = None     # connections map

    @property
    def colmap(self):
        return self._colmap

    @property
    def celmap(self):
        return self._celmap

    @property
    def segmap(self):
        return self._segmap

    @property
    def synmap(self):
        return self._synmap

    @property
    def ncolumns(self):
        return self.getcfg('ncols')

    @property
    def ncells(self):
        return self.getcfg('ncels')

    @property
    def nsegments(self):
        return self.getcfg('nsegs')

    @property
    def nsynapses(self):
        return self.getcfg('nsyns')

    @ncolumns.setter
    def ncolumns(self, n: int):
        MAX = self.getcfg('max_ncols')
        if n > MAX:
            self.setcfg('ncols', n)
        else:
            raise Exception('Exceeded maximum number of columns. (max: {}, set: {})'.format(MAX, n))

    @ncells.setter
    def ncells(self, n: int):
        MAX = self.getcfg('max_ncels')
        if n > MAX:
            self.setcfg('ncels', n)
        else:
            raise Exception('Exceeded maximum number of cells per column. (max: {}, set: {})'.format(MAX, n))

    @nsegments.setter
    def nsegments(self, n: int):
        MAX = self.getcfg('max_nsegs')
        if n > MAX:
            self.setcfg('nsegs', n)
        else:
            raise Exception('Exceeded maximum number of segments per cell. (max: {}, set: {})'.format(MAX, n))

    @nsynapses.setter
    def nsynapses(self, n: int):
        MAX = self.getcfg('max_nsyns')
        if n > MAX:
            self.setcfg('nsyns', n)
        else:
            raise Exception('Exceeded maximum number of synapses per segment. (max: {}, set: {})'.format(MAX, n))

    def init_columns(self):
        self._colmap = np.zeros((self.ncolumns, 1), dtype=bool)

    def init_cells(self):
        self._celmap = np.zeros((self.ncolumns, self.ncells), dtype=bool)

    def init_segments(self):
        self._segmap = np.zeros((self.ncolumns, self.ncells, self.nsegments), dtype=bool)

    def init_synapses(self):
        self._synmap = np.zeros((self.ncolumns, self.ncells, self.nsegments, self.nsynapses), dtype=bool)

    def configure(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def compute(self, input, output, islearn):
        raise NotImplementedError

    def render(self, tmap):
        raise NotImplementedError
