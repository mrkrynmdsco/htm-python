
from htm.core.common import htmObj
from htm.core.common import htmState


SYN_DEF_LR = 0.03   # Synapse default learn rate
SYN_DEF_CT = 0.6    # Synapse default connection threshold
SYN_MIN_CT = 0.3    # Synapse minimum connection threshold
SYN_MAX_CT = 0.75   # Synapse maximum connection threshold

SYN_MIN_PERM = 0.0  # Synapse minimum permanence (default)
SYN_MAX_PERM = 1.0  # Synapse maximum pemanence


class Synapse (htmObj):
    """ HTM Synapse """

    def __init__(self):
        super().__init__()

        self._state = htmState.INACTIVE
        self._learn_rate = SYN_DEF_LR
        self._conn_thres = SYN_DEF_CT
        self._permanence = SYN_MIN_PERM
        self._conn_index = None

    # GETTER FUNCTIONS
    # ----------------

    @property
    def state(self):
        return self._state

    @property
    def learn_rate(self):
        return self._learn_rate

    @property
    def connection_threshold(self):
        return self._conn_thres

    @property
    def permanence(self):
        return self._permanence

    @property
    def connection_index(self):
        return self._conn_index

    # SETTER FUNCTIONS
    # ----------------

    @state.setter
    def state(self, s: htmState):
        if s in [htmState.INACTIVE, htmState.ACTIVE]:
            self._state = s
        else:
            raise Exception('Unknown Synapse state being set.')

    @learn_rate.setter
    def learn_rate(self, lr: float):
        if SYN_MIN_PERM <= lr <= SYN_MAX_PERM:
            self._learn_rate = lr
        else:
            if SYN_MAX_PERM < lr:
                self.learn_rate = SYN_MAX_PERM
            if SYN_MIN_PERM > lr:
                self.learn_rate = SYN_MIN_PERM

    @connection_threshold.setter
    def connection_threshold(self, ct: float):
        if SYN_MIN_CT <= ct <= SYN_MAX_CT:
            self._conn_thres = ct
        else:
            if SYN_MAX_CT < ct:
                self._conn_thres = SYN_MAX_CT
            if SYN_MIN_CT > ct:
                self._conn_thres = SYN_MIN_CT

    @permanence.setter
    def permanence(self, p: float):
        if SYN_MIN_PERM <= p <= SYN_MAX_PERM:
            self._permanence = p
        else:
            if SYN_MAX_PERM < p:
                self._permanence = SYN_MAX_PERM
            if SYN_MIN_PERM > p:
                self._permanence = SYN_MIN_PERM

    @connection_index.setter
    def connection_index(self, ci: int):
        self._conn_index = ci

    # METHODS
    # -------

    def update(self):
        # permanence
        # state
        pass


class Dendrite:
    """ HTM Dendrite """

    def __init__(self):
        self._is_active = False
        self._thres = 12
        self._synapses = []

    # GETTER FUNCTIONS
    # ----------------

    @property
    def is_active(self):
        return self._is_active

    # METHODS
    # -------

    def syns_sdr(self):
        pass

    def update(self):
        pass


class Cell(htmObj):
    """ HTM Cell """

    def __init__(self, idx: int):
        super().__init__(idx=idx)
        self._thres = None
        self._state = None

    # GETTER FUNCTIONS
    # ----------------

    @property
    def activation_threshold(self):
        return self._thres

    @property
    def state(self):
        return self._state

    # SETTER FUNCTIONS
    # ----------------

    @activation_threshold.setter
    def activation_threshold(self, t: float):
        self._thres = t

    @state.setter
    def state(self, s: htmState):
        self._state = s


class Neuron(Cell):
    """ HTM Neuron Cell """

    def __init__(self, idx: int = 0):
        super().__init__(idx=idx)

        self.proximal = [None]  # proximal dendrite

        self.tx_distals = []  # transmit-distal dendrites
        self.rx_distals = []  # recieve-distal dendrites

        self.state = htmState().INACTIVE  # default cell state

    def update(self):
        # Inactive
        # Active
        # Predictive
        pass
