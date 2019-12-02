
import unittest as ut
from htm.core.common import htmObj, htmState
from htm.core.neocortex import Synapse


class Synapse_InitTests(ut.TestCase):

    def setUp(self):
        self.syn = Synapse()

    def test_object_instance(self):
        # HTM-FR_SYN_01
        self.assertIsInstance(self.syn, htmObj)

    def test_default_state(self):
        # HTM-FR_SYN_02
        self.assertEqual(self.syn.state, htmState.INACTIVE)

    def test_default_permanence(self):
        # HTM-FR_SYN_03
        self.assertEqual(self.syn.permanence, 0.0)

    def test_default_connection_thres(self):
        # HTM-FR_SYN_05
        self.assertEqual(self.syn.connection_threshold, 0.6)

    def test_default_learn_rate(self):
        # HTM-FR_SYN_07
        self.assertEqual(self.syn.learn_rate, 0.03)

    def test_default_connection_idx(self):
        # HTM-FR_SYN_08
        self.assertEqual(self.syn.connection_index, None)


class Synapse_UseTests(ut.TestCase):

    def setUp(self):
        self.syn = Synapse()

    def test_set_permanence(self):
        # HTM-FR_SYN_03
        self.syn.permanence = 0.1
        self.assertEqual(self.syn.permanence, 0.1)

    def test_set_permanence_beyond_limits(self):
        # HTM-FR_SYN_03
        self.syn.permanence = 1.1
        self.assertEqual(self.syn.permanence, 1.0)
        self.syn.permanence = -0.9
        self.assertEqual(self.syn.permanence, 0.0)

    def test_increase_permanence(self):
        # HTM-FR_SYN_04
        self.syn.learn_rate = 0.2
        self.syn.permanence = 0.6
        self.syn.increase_permanence()
        self.assertEqual(self.syn.permanence, 0.8)

    def test_decrease_permanence(self):
        # HTM-FR_SYN_04
        self.syn.learn_rate = 0.4
        self.syn.permanence = 0.6
        self.syn.decrease_permanence()
        self.assertEqual(self.syn.permanence, 0.2)

    def test_set_connection_thres(self):
        # HTM-FR_SYN_05
        self.syn.connection_threshold = 0.4
        self.assertEqual(self.syn.connection_threshold, 0.4)

    def test_set_connection_thres_beyond_limits(self):
        # HTM-FR_SYN_05
        self.syn.connection_threshold = 0.8
        self.assertEqual(self.syn.connection_threshold, 0.75)
        self.syn.connection_threshold = 0.29
        self.assertEqual(self.syn.connection_threshold, 0.3)

    def test_set_learn_rate(self):
        # HTM-FR_SYN_07
        self.syn.learn_rate = 0.1
        self.assertEqual(self.syn.learn_rate, 0.1)

    def test_set_learn_rate_beyond_limits(self):
        # HTM-FR_SYN_07
        self.syn.learn_rate = 1.1
        self.assertEqual(self.syn.learn_rate, 1.0)
        self.syn.learn_rate = -0.9
        self.assertEqual(self.syn.learn_rate, 0.0)
