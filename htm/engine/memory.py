
from htm.types.base import MemoryHTM


class InputMemory (MemoryHTM):
    """ HTM Input Memory """

    def __init__(self):
        super().__init__()
        # Delete unnecessary attributes
        del self._segmap
        del self._synmap
        del self._conmap

        self.setcfg('input_shape', None)

    def configure(self, shape: tuple):
        self.setcfg('input_shape', shape)
        self.setcfg('max_ncols', shape[0] * shape[1])
        self.setcfg('max_ncels', 1)

        self.ncolumns = self.getcfg('max_ncols')
        self.ncells = self.getcfg('max_ncels')

    def initialize(self):
        self.init_columns()
        self.init_cells()


class SpatialMemory (MemoryHTM):
    """ HTM Spatial Memory """

    def __init__(self):
        super().__init__()
        cfg = {
            'input_shape': (32, 32),
            'column_shape': (64, 64),
            'potential_radius': 16,
            'potential_percentage': 0.50,
            'global_inhibition': False,
            'local_area_density': 0.02,
            'threshold_stimulus': 1,
            'threshold_permanence': 0.10,
            'permanence_increment': 0.10,
            'permanence_decrement': 0.01,
            'min_overlap_pct_duty': 0.001,
            'duty_cycle_period': 1000,
            'boost_strength': 1.0,
            'seed': 1,
            'verbosity': 0,
            'wrap_around': True
        }
        self.append_cfgs(cfg)

        self._inhmap = None     # columns inhibition map
        self._permap = None     # synapses permanence map


class TemporalMemory (MemoryHTM):
    """ HTM Temporal Memory """

    def __init__(self):
        super().__init__()

        self._prdmap = None     # cells prediction map


class SpatioTemporalMemory (MemoryHTM):
    """ HTM Spatio-Temporal Memory """

    def __init__(self):
        super().__init__()
        self._sp = None
        self._tp = None
