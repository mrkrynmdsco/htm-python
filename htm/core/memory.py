
class Memory:
    """ HTM Memory """

    def __init__(self):
        self._size = None


class InputMemory(Memory):
    """ HTM Input Memory """

    def __init__(self):
        super().__init__()
        pass


class SpatialMemory(Memory):
    """ HTM Spatial Memory """

    def __init__(self):
        super().__init__()
        pass


class TemporalMemory(Memory):
    """ HTM Temporal Memory """

    def __init__(self):
        super().__init__()
        pass


class IM(InputMemory):
    """ Alias for InputMemory Class """
    pass


class SM(SpatialMemory):
    """ Alias for HTM SpatialMemory Class """
    pass


class TM(TemporalMemory):
    """ Alias for HTM TemporalMemory Class """
    pass
