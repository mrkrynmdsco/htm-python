
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

    def getcfg(self, key: str):
        return self._cfg[key]

    def setcfg(self, key: str, value):
        self._cfg[key] = value

    def getcfgs(self):
        return self._cfg

    def setcfgs(self, cfgs: dict):
        self._cfg = cfgs

    def append_cfgs(self, cfgs: dict):
        for key, value in cfg.items():
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

        self._inhmap = None     # column inhibition map
        self._prdmap = None     # cell prediction map

    def get_ncolumns(self):
        return self.getcfg('ncols')

    def get_ncells(self):
        return self.getcfg('ncels')

    def get_nsegments(self):
        return self.getcfg('nsegs')

    def get_nsynapses(self):
        return self.getcfg('nsyns')

    def set_ncolumns(self, n: int):
        self.setcfg('ncols', n)

    def set_ncells(self, n: int):
        self.setcfg('ncels', n)

    def set_nsegments(self, n: int):
        self.setcfg('nsegs', n)

    def set_nsynapses(self, n: int):
        self.setcfg('nsyns', n)

    def init_columns(self):
        self._colmap = torch.BoolTensor([0] * self.get_ncolumns())

    def init_cells(self):
        self._celmap = torch.BoolTensor([[0] * self.get_ncells()] * self.get_ncolumns())

    def configure(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def compute(self, input, output, islearn):
        raise NotImplementedError

    def render(self, tmap):
        raise NotImplementedError
