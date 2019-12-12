
from htm.types.base import BaseHTM


class Synapse (BaseHTM):
    """ HTM Synapse (input slot) """

    def __init__(self):
        super().__init__()
        self._cfg = {
            'syn_th': 0.5,  # permanence threshold for when a connection is formed [0, 1]
            'pinc': 0.03,   # permanence increment amount
            'pdec': 0.05,   # permanence decrement amount
            'ptol': 0.05,   # tolerance amount from syn_th used to determine how the permanence be initialized
        }

    def randomize_permanence(self, option):
        pass


class Segment (BaseHTM):
    """ HTM Segment (dendrite) """

    def __init__(self):
        super().__init__()
        self._cfg = {
            'nsynapses': 10,    # number of synapses in this segment
            'seg_th': 1,        # number of synapses to be active for the segment to be active
        }


class Cell (BaseHTM):
    pass


class Column (BaseHTM):
    """ HTM Column (mini-column) """

    def __init__(self):
        super().__init__()
        self._cfg = {
            'ncells': 3,            # number of cell in this column
            'max_boost': 10,        # maximum boosting value
            'duty_cycle': 1000,     # duty cycle to use for boosting
        }
