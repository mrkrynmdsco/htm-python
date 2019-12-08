
from enum import Enum


class BaseHTM:
    def __init__(self):
        self._index = None
        self._state = None
        self._cfg = {}

    def get_index(self):
        return self._index

    def get_state(self):
        return self._state

    def get_config(self, key):
        return self._cfg[key]

    def get_configs(self):
        return self._cfg

    def set_index(self, i: int):
        self._index = i

    def set_state(self, s):
        raise NotImplementedError

    def set_config(self, key, value):
        self._cfg[key] = value

    def set_configs(self, cfg: dict):
        self._cfg = cfg

    def update(self):
        raise NotImplementedError


class StateHTM (Enum):
    PREDICTED = -1
    INACTIVE = False
    ACTIVE = True


PREDICTED = StateHTM.PREDICTED
INACTIVE = StateHTM.INACTIVE
ACTIVE = StateHTM.ACTIVE


class Synapse (BaseHTM):
    """ HTM Synapse """
    def __init__(self):
        super().__init__()
        self._cfg = {
            'learn_rate': 0.003,
            'threshold_connect': 0.3,
            'min_permanence': 0.0,
            'max_permanence': 1.0,
        }
        self._srcid = None
        self._state = INACTIVE

        self._isconn = False
        self._permanence = 0.0

    def isconnected(self):
        return self._isconn

    def get_source_index(self):
        return self._srcid

    def get_permanence(self):
        return self._permanence

    def set_source_index(self, idx: int):
        self._srcid = idx

    def set_state(self, s: StateHTM):
        self._state = s

    def set_permanence(self, p: float):
        MIN_P = self.get_config('min_permanence')
        MAX_P = self.get_config('max_permanence')

        if MIN_P <= p <= MAX_P:
            self._permanence = p
        elif MIN_P > p:
            self._permanence = MIN_P
        elif MAX_P < p:
            self._permanence = MAX_P
        else:
            raise Exception('Invalid permanence value being set: {}'.format(p))

    def _update_connection(self):
        p = self.get_permanence()
        t = self.get_config('threshold_connect')

        if p >= t:
            self._isconn = True
        else:
            self._isconn = False

    def increase_permanence(self):
        p = self.get_permanence()
        p = round(p + self.get_config('learn_rate'), 9)
        self.set_permanence(p)
        self._update_connection()

    def decrease_permanence(self):
        p = self.get_permanence()
        p = round(p - self.get_config('learn_rate'), 9)
        self.set_permanence(p)
        self._update_connection()

    def update(self):
        # update the state of this synapse
        # by calling a function (e.g. from a pooler)
        # to fetch the current state of the cell (axon)
        # connected to it
        pass


class Dendrite (BaseHTM):
    """ HTM Dendrite """
    def __init__(self):
        super().__init__()
        self._cfg = {
            'threshold_active': 6,
            'min_synapse': 9,
            'max_synapse': 18,
        }

        self._synapses = []
        self._state = INACTIVE

    def get_synapses(self, s: StateHTM = None):
        onsyns = []
        offsyns = []

        for s in self._synapses:
            if ACTIVE ==  s.get_state():
                onsyns.append(s)
            if INACTIVE ==  s.get_state():
                offsyns.append(s)

        if None == s:
            return onsyns, offsyns
        if INACTIVE == s:
            return offsyns
        if ACTIVE == s:
            return onsyns

    def add_synapse(self, srcid):
        MAX_NS = self.get_config('max_synapse')
        nsyns = len(self.get_active_synapses())

        if MAX_NS >= nsyns:
            s = Synapse()
            s.set_source_index(srcid)
            self._synapse.append(s)

    def del_synapse(self, idx):
        raise NotImplementedError

    def _update_state(self):
        for s in self._synapses:
            s.update()

        n = len(self.get_synapses(s=ACTIVE))
        t = self.get_config('threshold_active')

        if n >= t:
            self.set_state(s=ACTIVE)
        else:
            self.set_state(s=INACTIVE)

    def update(self):
        self._update_state()


class Cell (BaseHTM):
    """ HTM Cell """
    def __init__(self):
        super().__init__()
        self._cfg = {
            'min_distals': 2,
            'max_distals': 12,
        }

        self._state = INACTIVE
        self._proximal = None
        self._distals = []

    def update(self):
        pass
