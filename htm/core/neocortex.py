
from htm.core.common import htmObj
from htm.core.common import htmState


class Synapse:
    """ HTM Synapse """

    def __init__(self):
        self._learn_rate = 0.03
        self._conn_thres = 0.6
        self._permanence = 0.0

    # GETTER FUNCTIONS
    # ----------------

    @property
    def learn_rate(self):
        return self._learn_rate

    @property
    def connection_threshold(self):
        return self._conn_thres

    @property
    def permanence(self):
        return self._permanence

    # SETTER FUNCTIONS
    # ----------------

    @learn_rate.setter
    def learn_rate(self, lr: float):
        self._learn_rate = lr

    @connection_threshold.setter
    def connection_threshold(self, ct: float):
        self._conn_thres = ct

    @permanence.setter
    def permanence(self, p: float):
        self._permanence = p


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
