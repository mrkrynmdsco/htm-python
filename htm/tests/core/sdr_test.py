
import unittest as ut
from htm.core.sdr import SDR


class SDR_InitializationTest(ut.TestCase):

    def setUp(self):
        sdr = SDR()

    def test_dummy(self):
        self.assertTrue(True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    ut.main()
