
from htm.core.common import htmObj
from htm.core.common import SynapseState
from htm.core.common import DendriteState
from htm.core.common import CellState


SYN_DEF_LR = 0.03   # Synapse default learn rate
SYN_DEF_AT = 0.6    # Synapse default activation threshold
SYN_MIN_AT = 0.3    # Synapse minimum activation threshold
SYN_MAX_AT = 0.75   # Synapse maximum activation threshold
SYN_MIN_PERM = 0.0  # Synapse minimum permanence (default)
SYN_MAX_PERM = 1.0  # Synapse maximum pemanence

UNCONNECTED = SynapseState.UNCONNECTED
CONNECTED = SynapseState.CONNECTED

OFF = DendriteState.OFF
ON = DendriteState.ON

INACTIVE = CellState.INACTIVE
ACTIVE = CellState.ACTIVE
PREDICTED = CellState.PREDICTED

ROUND_DP = 9        # rounding-off decimal place


class Synapse (htmObj):
    """ HTM Synapse """

    def __init__(self):
        super().__init__()

        self._state = UNCONNECTED
        self._lrate = SYN_DEF_LR
        self._thres = SYN_DEF_AT
        self._perma = SYN_MIN_PERM
        self._inputidx = None
        self._inputsig = None

    # GETTER FUNCTIONS
    # ----------------

    @property
    def state(self):
        return self._state

    @property
    def learn_rate(self):
        return self._lrate

    @property
    def activation_threshold(self):
        return self._thres

    @property
    def permanence(self):
        return self._perma

    @property
    def input_index(self):
        return self._inputidx

    @property
    def input_signal(self):
        return self._inputsig

    # SETTER FUNCTIONS
    # ----------------

    @state.setter
    def state(self, s: SynapseState):
        if s in [UNCONNECTED, CONNECTED]:
            self._state = s
        else:
            raise Exception('Unknown Synapse state being set.')

    @learn_rate.setter
    def learn_rate(self, lr: float):
        if SYN_MIN_PERM <= lr <= SYN_MAX_PERM:
            self._lrate = lr
        else:
            if SYN_MAX_PERM < lr:
                self._lrate = SYN_MAX_PERM
            if SYN_MIN_PERM > lr:
                self._lrate = SYN_MIN_PERM

    @activation_threshold.setter
    def activation_threshold(self, thres: float):
        if SYN_MIN_AT <= thres <= SYN_MAX_AT:
            self._thres = thres
        else:
            if SYN_MAX_AT < thres:
                self._thres = SYN_MAX_AT
            if SYN_MIN_AT > thres:
                self._thres = SYN_MIN_AT

    @permanence.setter
    def permanence(self, p: float):
        if SYN_MIN_PERM <= p <= SYN_MAX_PERM:
            self._perma = p
        else:
            if SYN_MAX_PERM < p:
                self._perma = SYN_MAX_PERM
            if SYN_MIN_PERM > p:
                self._perma = SYN_MIN_PERM

    @input_index.setter
    def input_index(self, idx: int):
        self._inputidx = idx

    @input_signal.setter
    def input_signal(self, sig):
        self._inputsig = sig

    # METHODS
    # -------
    def increase_permanence(self):
        self.permanence = round((self.permanence + self.learn_rate), ROUND_DP)

    def decrease_permanence(self):
        self.permanence = round((self.permanence - self.learn_rate), ROUND_DP)

    def read_input(self):
        # scan the state of the input
        # store the state of the input
        raise NotImplementedError

    def update_state(self):
        if self.permanence >= self.activation_threshold:
            self.state = CONNECTED
        else:
            self.state = UNCONNECTED

    def update(self):
        # self.read_input()
        self.update_state()


class Dendrite (htmObj):
    """ HTM Dendrite """

    def __init__(self, nsynapse: int):
        super().__init__()

        self._state = INACTIVE
        self._thres = 12
        self._synapses = None

    # GETTER FUNCTIONS
    # ----------------

    @property
    def state(self):
        return self._state

    # SETTER FUNCTIONS
    # ----------------

    @state.setter
    def state(self, s: DendriteState):
        if s in [OFF, ON]:
            self._state = s
        else:
            raise Exception('Unknown Dendrite state being set.')

    # METHODS
    # -------

    def update(self):
        pass


class Cell (htmObj):
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
    def activation_threshold(self, thres: float):
        self._thres = thres

    @state.setter
    def state(self, s: CellState):
        if s in [INACTIVE, ACTIVE, PREDICTIVE]:
            self._state = s
        else:
            raise Exception('Unknown Cell state being set.')


class Neuron (Cell):
    """ HTM Neuron Cell """

    def __init__(self, idx: int = 0):
        super().__init__(idx=idx)

        self.proximal = [None]  # proximal dendrite

        self.tx_distals = []  # transmit-distal dendrites
        self.rx_distals = []  # recieve-distal dendrites

        self.state = CellState.INACTIVE  # default cell state

    def update(self):
        # Inactive
        # Active
        # Predictive
        pass
