
from htm.types.base import Map


class PermanenceMap (Map):
    pass


class ConnectionMap (Map):
    """ Connection Map (htm) """

    def __init__(self, size: int):
        super().__init__(size=size)
        self.initialize()

    def initialize(self):
        self._map = [[] for i in range(self.size)]

    def get_connection(self, idx: int):
        return self.map[idx]

    def add_connection(self, idx: int, to_idx: int):
        if to_idx not in self.map[idx]:
            self.map[idx].append(to_idx)

    def del_connection(self, idx: int, to_idx: int):
        if to_idx in self.map[idx]:
            self.map[idx].remove(to_idx)

    def add_connections(self, idx: int, ilst: list):
        for i in ilst:
            self.add_connection(idx, i)

    def del_connections(self, idx: int, ilst: list):
        for i in ilst:
            self.del_connection(idx, i)


class DistalStateMap (Map):
    pass


class CellStateMap (Map):
    pass


class ColumnStateMap (Map):
    pass


class FeedForwardMap (Map):
    pass


class FeedBackwardMap (Map):
    pass


class ReceptiveFieldMap (Map):
    pass


class InhibitionRadiusdMap (Map):
    pass


class PredictionMap (Map):
    pass
