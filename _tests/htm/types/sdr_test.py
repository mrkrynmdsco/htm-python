
import unittest as ut
import torch
import torch.cuda as cuda
from htm.types.sdr import SDR


DEF_BITRES = 12
DEF_NBITS = 4096
DEF_SPARSE_PCT = 0.02
DEF_ON_BITS = 81


class SDR_InitTests(ut.TestCase):

    def setUp(self):
        self.sdr = SDR()

    def test_default_bit_resolution(self):
        self.assertEqual(self.sdr.bitres, DEF_BITRES)
        self.assertIsInstance(self.sdr.bitres, int)

    def test_default_cell_count(self):
        self.assertEqual(self.sdr.nbits, DEF_NBITS)
        self.assertIsInstance(self.sdr.nbits, int)

    def test_default_sparsity(self):
        self.assertEqual(self.sdr.sparsity, DEF_SPARSE_PCT)
        self.assertIsInstance(self.sdr.sparsity, float)

    def test_default_active_cells(self):
        self.assertEqual(self.sdr.wbits, DEF_ON_BITS)
        self.assertIsInstance(self.sdr.wbits, int)

    def test_default_formats(self):
        self.assertListEqual(self.sdr.sparse, [])
        self.assertListEqual(self.sdr.coords, [])
        self.assertListEqual(self.sdr.dense().tolist(), [False]*self.sdr.nbits)

    def test_default_device_allocation(self):
        if cuda.is_available():
            self.assertEqual(self.sdr.device, 'cuda')
        else:
            self.assertEqual(self.sdr.device, 'cpu')


class SDR_UseTests(ut.TestCase):

    def test_set_bit_resolution(self):
        self.sdr = SDR(bitres=10)
        self.assertEqual(self.sdr.bitres, 10)
        self.assertEqual(self.sdr.nbits, 1024)

        self.sdr.bitres = 8
        self.assertEqual(self.sdr.bitres, 8)
        self.assertEqual(self.sdr.nbits, 256)

    def test_set_sparsity(self):
        self.sdr = SDR(sprpct=0.5)
        self.assertEqual(self.sdr.sparsity, 0.5)
        self.assertEqual(self.sdr.wbits, 2048)

        self.sdr.sparsity = 0.02
        self.assertEqual(self.sdr.sparsity, 0.02)
        self.assertEqual(self.sdr.wbits, 81)

    def test_set_sparse(self):
        self.sdr = SDR(bitres=3, sprpct=0.5)
        self.sdr.sparse = [1, 2, 5, 6]
        if 'cuda' == self.sdr.device:
            self.assertIsInstance(self.sdr.sparse, cuda.IntTensor)
        else:
            self.assertIsInstance(self.sdr.sparse, torch.IntTensor)

        self.assertListEqual(self.sdr.sparse.tolist(), [1, 2, 5, 6])
        self.assertListEqual(self.sdr.dense(raw=False).tolist(), [0, 1, 1, 0, 0, 1, 1, 0])

    # def test_set_coords(self):
    #     self.sdr = SDR(bitres=3, sprpct=0.25)
    #     if 'cuda' == self.sdr.device:
    #         self.assertIsInstance(self.sdr.coords, cuda.IntTensor)
    #     else:
    #         self.assertIsInstance(self.sdr.coords, torch.IntTensor)
    #     # FIXME Failing


if __name__ == '__main__':
    ut.main()
