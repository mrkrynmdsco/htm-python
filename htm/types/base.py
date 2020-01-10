
import torch
import torch.cuda as cuda


class _htmObj_ (object):
    """ HTM Base Object """

    def __init__(self):
        self._cfg = {}
        self._device = 'cuda' if cuda.is_available() else 'cpu'

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
        self._map = [[] for i in range(self.size)]


class Connections (Map):
    """ Connections Map (htm) """

    def __init__(self, size: int):
        super().__init__(size=size)
        cfg = {
            'max_conns': 16,    # maximum number of connections per map cell
            'min_conns': 4,     # minimum number of connections per map cell
        }
        self.append_cfgs(cfg)

        self.initialize()

    def add_connection(self, idx: int, to_idx: int):
        if to_idx not in self.map[idx] and self.getcfg('max_conns') > len(self.map[idx]):
            self.map[idx].append(to_idx)

    def del_connection(self, idx: int, to_idx: int):
        if to_idx in self.map[idx]:
            self.map[idx].remove(to_idx)

    def get_connections(self, idx: int):
        return self.map[idx]


class Memory (_htmObj_):
    """ Memory (htm) """
    
    def __init__(self, size: int):
        super().__init__()
        cfg = {
            'size': None,
            'max_size': None,
            'min_size': None,
        }
        self.setcfgs(cfg)




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


class MemoryHTM (_htmObj_):
    """ HTM Memory Object """

    def __init__(self):
        super().__init__()
        cfg = {
            'ncols': None,      # number of columns
            'ncels': None,      # number of cells per column
            'nsegs': None,      # number of segments per cell
            'nsyns': None,      # number of synapses per segment

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

    def create_columns(self):
        self._colmap = torch.zeros(size=(self.ncolumns, 1),
                                   dtype=torch.bool,
                                   device=self._device)

    def create_cells(self):
        self._celmap = torch.zeros(size=(self.ncolumns, self.ncells),
                                   dtype=torch.bool,
                                   device=self._device)

    def create_segments(self):
        self._segmap = torch.zeros(size=(self.ncolumns, self.ncells, self.nsegments),
                                   dtype=torch.bool,
                                   device=self._device)

    def create_synapses(self):
        self._synmap = torch.zeros(size=(self.ncolumns, self.ncells, self.nsegments, self.nsynapses),
                                   dtype=torch.bool,
                                   device=self._device)

    def configure(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def compute(self, input, output, islearn):
        raise NotImplementedError

    def render(self, tmap):
        raise NotImplementedError
