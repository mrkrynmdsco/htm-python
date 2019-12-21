
import unittest as ut
from htm.types.base import ObjectHTM


class ObjectHTM_BasicTests(ut.TestCase):
    def setUp(self):
        self.obj = ObjectHTM()

    def test_default_property_values(self):
        self.assertEqual(self.obj.getcfgs(), {})

    def test_setter_functions(self):
        self.obj.setcfg('max_value', 69)
        self.assertEqual(self.obj.getcfg('max_value'), 69)

        cfg = {'min_value': 3}
        self.obj.setcfgs(cfg)
        self.assertEqual(self.obj.getcfgs(), cfg)
