
from htm.core.cortex import BaseHTM
from htm.core.cortex import Cell


def populate_column(ncells: int):
    c = []
    for i in range(ncells):
        n = Cell()
        n.index = i
        c.append(n)
    return c


class Column (BaseHTM):
    """ HTM Column (mini-column) """
    def __init__(self):
        super().__init__()

        self._cells = None

    def boost(self):
        pass

    def inhibit(self):
        pass

    def cells_sdr(self):
        pass

    def update(self):
        pass


class HyperColumn (BaseHTM):
    """ HTM Hyper Column (macro-column) """
    def __init__(self):
        super().__init__()


class Layer:
    """ HTM Layer """
    def __init__(self):
        pass


class Region:
    """ HTM Region """
    def __init__(self):
        self._columns = None

    def cols_sdr(self):
        pass


class Network:
    """ HTM Network """

    def __init__(self):
        pass
