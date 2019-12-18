
import sys
sys.path.append('../')

import torch
from memory_profiler import profile
from htm.types.base import MemoryHTM


@profile
def init_columns():
    m = MemoryHTM()
    m.set_ncolumns(4096)
    m._colmap = torch.BoolTensor([0]*m.get_ncolumns())

    return m


@profile
def init_cells():
    m = MemoryHTM()
    m.set_ncolumns(4096)
    m.set_ncells(4)
    m._celmap = torch.BoolTensor([[0] * m.get_ncells()] * m.get_ncolumns())

    return m


@profile
def init_colscels():
    m = MemoryHTM()
    m.set_ncolumns(4096)
    m.set_ncells(4)
    m._colmap = torch.BoolTensor([0] * m.get_ncolumns())
    m._celmap = torch.BoolTensor([[0] * m.get_ncells()] * m.get_ncolumns())

    return m


if __name__ == "__main__":
    # m = init_columns()
    # print(m._colmap)

    # m = init_cells()
    # print(m._celmap)

    m = init_colscels()
    print(m._colmap)
    print(m._celmap)
