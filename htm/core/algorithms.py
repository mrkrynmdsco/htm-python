
class Connections:
    pass


class Memory:
    """ HTM Memory """

    def __init__(self):
        self._input_space = None
        self._column_dims = None


class SpatialMemory(Memory):
    """ HTM Spatial Memory """

    def __init__(self):
        super().__init__()
        self._potential_rad = None
        self._potential_pct = None


class TemporalMemory(Memory):
    """ HTM Temporal Memory """

    def __init__(self):
        super().__init__()
        pass


class SM(SpatialMemory):
    """ Alias for HTM SpatialMemory Class """
    pass


class TM(TemporalMemory):
    """ Alias for HTM TemporalMemory Class """
    pass
