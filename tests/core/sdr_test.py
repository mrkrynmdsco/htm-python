
import unittest as ut
import torch
import torch.cuda as cuda
from htm.core.sdr import SDR


DEF_BITRES = 12
DEF_NCELLS = 4096
DEF_SPARSE_PCT = 0.02
DEF_ON_CELLS = 81


class SDR_InitializationTests(ut.TestCase):

    def setUp(self):
        self.sdr = SDR()

    def test_default_bit_resolution(self):
        self.assertEqual(self.sdr.resolution, DEF_BITRES)
        self.assertIsInstance(self.sdr.resolution, int)

    def test_default_cell_count(self):
        self.assertEqual(self.sdr.ncells, DEF_NCELLS)
        self.assertIsInstance(self.sdr.ncells, int)

    def test_default_sparsity(self):
        self.assertEqual(self.sdr.sparsity, DEF_SPARSE_PCT)
        self.assertIsInstance(self.sdr.sparsity, float)

    def test_default_active_cells(self):
        self.assertEqual(self.sdr.wcells, DEF_ON_CELLS)
        self.assertIsInstance(self.sdr.wcells, int)

    def test_default_dense_tensor(self):
        if cuda.is_available():
            self.assertIsInstance(self.sdr.dense, cuda.BoolTensor)
        else:
            self.assertIsInstance(self.sdr.dense, torch.BoolTensor)

        self.assertEqual(self.sdr.dense.size(), torch.Size([DEF_NCELLS]))

    def test_default_sparse_tensor(self):
        self.assertIsInstance(self.sdr.sparse, torch.IntTensor)
        self.assertEqual(self.sdr.sparse.size(), torch.Size([DEF_ON_CELLS]))


if __name__ == '__main__':
    ut.main()
