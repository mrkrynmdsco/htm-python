
from htm.types.base import MemoryHTM


class InputMemory (MemoryHTM):
    """ HTM Input Memory """

    def __init__(self):
        super().__init__()


class SpatialMemory (MemoryHTM):
    """ HTM Spatial Memory """

    def __init__(self):
        super().__init__()
        cfg = {
            'input_dimensions': (32, 32),
            'column_dimensions': (64, 64),
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
        self.append_configs(cfg)

        self._pooler = None

    def init_pooler(self):
        pass


class TemporalMemory (MemoryHTM):
    """ HTM Temporal Memory """

    def __init__(self):
        super().__init__()
        self._pooler = None


class SpatioTemporalMemory (MemoryHTM):
    """ HTM Spatio-Temporal Memory """

    def __init__(self):
        super().__init__()
        self._sp = None
        self._tp = None
