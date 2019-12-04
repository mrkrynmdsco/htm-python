
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


class Synapse (BaseHTM):
    """ HTM Synapse """
    def __init__(self):
        super().__init__()
        self._cfg = {
            'learn_rate': 0.003,
            'min_permanence': 0.0,
            'max_permanence': 1.0,
        }
        self._state = False
        self._permanence = 0.0

    def isconnected(self):
        if self.get_state():
            return True
        else:
            return False

    def get_permanence(self):
        return self._permanence

    def set_permanence(self, p: float):
        MIN = self.get_config('min_permanence')
        MAX = self.get_config('max_permanence')

        if MIN <= p <= MAX:
            self._permanence = p
        elif MIN > p:
            self._permanence = MIN
        elif MAX < p:
            self._permanence = MAX
        else:
            raise Exception('Invalid permanence value being set: {}'.format(p))

    def increase_permanence(self):
        p = self.get_permanence()
        p = round(p + self.get_config('learn_rate'), 9)
        self.set_permanence(p)

    def decrease_permanence(self):
        p = self.get_permanence()
        p = round(p - self.get_config('learn_rate'), 9)
        self.set_permanence(p)


class Dendrite (BaseHTM):
    """ HTM Dendrite """
    def __init__(self):
        super().__init__()

        self._synapses = None


class Cell (BaseHTM):
    """ HTM Cell """
    def __init__(self):
        super().__init__()

        self._proximal = None
        self._distals = None
