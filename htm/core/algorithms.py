
class InputSpace:
    """ HTM Input Space """

    def __init__(self):
        self._dimension = None


class Connections:
    pass


class SpatialPooler:
    """ HTM Spatial Pooler """

    def __init__(self):
        self._input_space = None
        self._column_dims = None

        self._potential_rad = None
        self._potential_pct = None


class TemporalMemory:
    pass


class SP(SpatialPooler):
    """ Alias for HTM SpatialPooler Class """
    pass


class TM(TemporalMemory):
    """ Alias for HTM TemporalMemory Class """
