
import unittest as ut
from htm.core.cortex import BaseHTM


class BaseHTM_BasicTests(ut.TestCase):
    def setUp(self):
        self.obj = BaseHTM()

    def test_default_property_values(self):
        self.assertEqual(self.obj.get_index(), None)
        self.assertEqual(self.obj.get_state(), None)
        self.assertEqual(self.obj.get_configs(), {})

    def test_setter_functions(self):
        self.obj.set_config('max_value', 69)
        self.assertEqual(self.obj.get_config('max_value'), 69)

        self.obj.set_index(69)
        self.assertEqual(self.obj.get_index(), 69)

        cfg = {'min_value': 3}
        self.obj.set_configs(cfg)
        self.assertEqual(self.obj.get_configs(), cfg)

        self.assertRaises(NotImplementedError, self.obj.set_state, 'any')