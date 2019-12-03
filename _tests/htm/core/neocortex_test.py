
import unittest as ut
from htm.core.common import (htmObj, SynapseState, DendriteState, CellState)
from htm.core.neocortex import Synapse
from htm.core.neocortex import Dendrite


class Synapse_InitTests(ut.TestCase):

    def setUp(self):
        self.syn = Synapse()

    def test_object_instance(self):
        # HTM-FR_SYN_01
        self.assertIsInstance(self.syn, htmObj)

    def test_default_state(self):
        # HTM-FR_SYN_02
        self.assertEqual(self.syn.state, SynapseState.UNCONNECTED)

    def test_default_permanence(self):
        # HTM-FR_SYN_03
        self.assertEqual(self.syn.permanence, 0.0)

    def test_default_activation_threshold(self):
        # HTM-FR_SYN_05
        self.assertEqual(self.syn.activation_threshold, 0.6)

    def test_default_learn_rate(self):
        # HTM-FR_SYN_07
        self.assertEqual(self.syn.learn_rate, 0.03)

    def test_default_source(self):
        # HTM-FR_SYN_08
        self.assertTupleEqual(self.syn.source, (None, None))


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

    def test_set_activation_threshold(self):
        # HTM-FR_SYN_05
        self.syn.activation_threshold = 0.4
        self.assertEqual(self.syn.activation_threshold, 0.4)

    def test_set_activation_threshold_beyond_limits(self):
        # HTM-FR_SYN_05
        self.syn.activation_threshold = 0.8
        self.assertEqual(self.syn.activation_threshold, 0.75)
        self.syn.activation_threshold = 0.29
        self.assertEqual(self.syn.activation_threshold, 0.3)

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


class Synapse_UpdateTests(ut.TestCase):

    def setUp(self):
        self.syn = Synapse()
        self.syn.activation_threshold = 0.6

    def test_update_state_inactive_active(self):
        # HTM-FR-SYN_06
        self.syn.state = SynapseState.UNCONNECTED
        self.syn.permanence = 0.6
        self.syn.update_state()
        self.assertEqual(self.syn.state, SynapseState.CONNECTED)

    def test_update_state_active_inactive(self):
        # HTM-FR-SYN_06
        self.syn.state = SynapseState.CONNECTED
        self.syn.permanence = 0.59
        self.syn.update_state()
        self.assertEqual(self.syn.state, SynapseState.UNCONNECTED)

    def test_update_function(self):
        # HTM-FR-SYN_09
        self.syn.state = SynapseState.UNCONNECTED
        self.syn.permanence = 0.59
        self.syn.update()
        self.assertEqual(self.syn.state, SynapseState.UNCONNECTED)
        self.syn.permanence = 0.69
        self.syn.update()
        self.assertEqual(self.syn.state, SynapseState.CONNECTED)


class Dendrite_InitTests(ut.TestCase):
    pass
