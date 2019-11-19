
import unittest as ut
from htm.core.sdr import SDR


DEF_NCELL = 2048
DEF_SPARSE_PCT = 0.02
DEF_ON_CELLS = 40


class SDR_InitializationTests(ut.TestCase):

    def test_default_cell_count(self):
        sdr = SDR()
        self.assertEqual(sdr.ncells, DEF_NCELL)
        self.assertIsInstance(sdr.ncells, int)

    def test_default_sparsity(self):
        sdr = SDR()
        self.assertEqual(sdr.sparsity, DEF_SPARSE_PCT)
        self.assertIsInstance(sdr.sparsity, float)

    def test_default_active_cells(self):
        sdr = SDR()
        self.assertEqual(sdr.wcells, DEF_ON_CELLS)
        self.assertIsInstance(sdr.wcells, int)


if __name__ == '__main__':
    ut.main()
