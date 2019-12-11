
from htm.core.algorithms import SpatialPooler


class Memory:
    """ HTM Memory """

    def __init__(self):
        self._size = None
        self._pooler = None
        self._cfg = {}

    def size(self):
        return self._size

    def pooler(self):
        return self._pooler

    def cfg(self, key):
        return self._cfg[key]

    def set_size(self, size):
        self._size = size

    def set_pooler(self, pooler):
        self._pooler = pooler

    def set_cfg(self, key, value):
        self._cfg[key] = value

    def compute(self, input, learn, output):
        raise NotImplementedError


class InputMemory (Memory):
    """ HTM Input Memory """

    def __init__(self, nbits: int):
        super().__init__()


class SpatialMemory (Memory):
    """ HTM Spatial Memory """

    def __init__(self):
        super().__init__()
        self._cfg = {
            'input_dimensions': (32, 32),
            'column_dimensions': (64, 64),
            'potential_radius': 16,
            'potential_percentage': 0.50,
            'global_inhibition': False,
            'local_area_density': 0.02,
            'threshold_stimulus': 1
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
        self._pooler = SpatialPooler()

    @property
    def pooler(self):
        return self._pooler


class TemporalMemory (Memory):
    """ HTM Temporal Memory """

    def __init__(self):
        super().__init__()
        pass
