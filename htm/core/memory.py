
from htm.types.base import Memory


class SpatialMemory (Memory):
    """ Spatial Memory (htm) """

    def __init__(self):
        super().__init__()
        cfg = {
            'input_shape': (128, 128),
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


class TemporalMemory (Memory):
    """ Temporal Memory (htm) """

    def __init__(self):
        super().__init__()
        cfg = {
            'input_shape': (128, 128),
        }
        self.append_cfgs(cfg)

        self._prdmap = None     # cells prediction map
