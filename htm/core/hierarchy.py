
from htm.core.common import htmObj
from htm.core.neocortex import Neuron


def _populate_column(ncells: int):
    c = []
    for i in range(ncells):
        c.append(Neuron(idx=i))
    return c


class Column(htmObj):
    """ HTM Column (mini-column)"""

    def __init__(self, idx: int = 0):
        super().__init__(idx=idx)

        self._cells = []

    def boost(self):
        pass

    def inhibit(self):
        pass

    def cells_sdr(self):
        pass

    def update(self):
        pass


class HyperColumn(htmObj):
    """ HTM Hyper Column (macro-column)"""

    def __init__(self, ncolumns: int):
        pass


class Layer:
    """ HTM Layer """

    def __init__(self):
        pass


class Region:
    """ HTM Region """

    def __init__(self):
        self._columns = []

    def cols_sdr(self):
        pass


class Network:
    """ HTM Network """

    def __init__(self):
        pass
