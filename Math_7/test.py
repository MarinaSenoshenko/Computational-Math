import unittest

from GaussZeydel import GaussZeydel
from HoleskyDecompozition import holeskyDecompozition
from LUdecompozition import LUDecompozition
from tridiagonalMatrixRunning import tridiagonalMatrixRunning


class MyTestCase(unittest.TestCase):
    def test_LUDecompozition_1(self):
        self.assertEqual(LUDecompozition([[5, 1, 0], [1, 5, 1], [0, 1, 5]], [1, 1, 1], 3), [0.17391304347826086, 0.13043478260869568, 0.17391304347826084])

    def test_holeskyDecompozition(self):
        self.assertEqual(holeskyDecompozition([[1, 0.5, 1./3.], [1./2., 1./3., 1./4.], [1./3., 1./4., 1./5.]], [2, 2, 2], 3), [6.000000000000011, -48.00000000000002, 60.00000000000001])

    def test_LUDecompozition_2(self):
        self.assertEqual(LUDecompozition([[4, -1, -1], [-1, 4, -1], [-1, -1, 4]], [2, 2, 2], 3), [1.0, 1.0, 0.9999999999999999])

    def test_LUDecompozition_3(self):
        self.assertEqual(LUDecompozition([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], [2, 2, 2], 3), [3.0, 4.0, 2.9999999999999996])

    def test_LUDecompozition_4(self):
        self.assertEqual(LUDecompozition([[2, -1], [-1, 2]], [1, 1], 2), [1.0, 1.0])

    def test_LUDecompozition_5(self):
        self.assertEqual(LUDecompozition([[1, 1, 2, 3], [1, 2, 3, -1], [3, -1, -1, -2], [2, 3, -1, -1]], [1, -4, -4, -6], 4), [-1.0, -1.0, -0.0, 1.0])

    def test_CaussZeydel_1(self):
        self.assertEqual(GaussZeydel([[4, -1, -1], [-1, 4, -1], [-1, -1, 4]], [2, 2, 2], 3, 0.000001), [0.9999998866405007, 0.9999999274059148, 0.9999999535116038])

    def test_CaussZeydel_2(self):
        self.assertEqual(GaussZeydel([[5, 1, 0], [1, 5, 1], [0, 1, 5]], [1, 1, 1], 3, 0.000001), [0.17391306342399998, 0.13043477463039999, 0.17391304507392])

    def test_CaussZeydel_3(self):
        self.assertEqual(GaussZeydel([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], [2, 2, 2], 3, 0.000001), [2.999999165534973, 3.999999165534973, 2.9999995827674866])

    def test_CaussZeydel_4(self):
        self.assertEqual(GaussZeydel([[2, -1], [-1, 2]], [1, 1], 2, 0.000001), [0.9999997615814209, 0.9999998807907104])

    def test_CaussZeydel_5(self):
        self.assertEqual(GaussZeydel([[2, -10], [-1, 2]], [1, 1], 2, 0.000001), 0)

    def test_tridiagonalMatrixRunning_1(self):
        self.assertEqual(tridiagonalMatrixRunning([[5, 1, 0], [1, 5, 1], [0, 1, 5]], [1, 1, 1]), [0.17391304347826086, 0.13043478260869568, 0.17391304347826084])

    def test_tridiagonalMatrixRunning_2(self):
        self.assertEqual(tridiagonalMatrixRunning([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], [2, 2, 2]), [3.0, 3.9999999999999996, 2.9999999999999996])

    def test_tridiagonalMatrixRunning_3(self):
        self.assertEqual(tridiagonalMatrixRunning([[2, -10, 0], [-1, 2, -1], [0, -1, 2]], [2, 2, 2]), 0)
