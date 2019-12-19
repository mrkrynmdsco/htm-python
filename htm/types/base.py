
import torch
import torch.cuda as cuda


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
            self.set_cfg(key, value)


class MemoryHTM (ObjectHTM):
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
        # TODO: Add checking against max limit
        self.setcfg('ncols', n)

    @ncells.setter
    def ncells(self, n: int):
        # TODO: Add checking against max limit
        self.setcfg('ncels', n)

    @nsegments.setter
    def nsegments(self, n: int):
        # TODO: Add checking against max limit
        self.setcfg('nsegs', n)

    @nsynapses.setter
    def nsynapses(self, n: int):
        # TODO: Add checking against max limit
        self.setcfg('nsyns', n)

    def init_columns(self):
        self._colmap = torch.zeros(size=(self.ncolumns, 1),
                                   dtype=torch.bool,
                                   device=self._device)

    def init_cells(self):
        self._celmap = torch.zeros(size=(self.ncolumns, self.ncells),
                                   dtype=torch.bool,
                                   device=self._device)

    def init_segments(self):
        self._segmap = torch.zeros(size=(self.ncolumns, self.ncells, self.nsegments),
                                   dtype=torch.bool,
                                   device=self._device)

    def init_synapses(self):
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
