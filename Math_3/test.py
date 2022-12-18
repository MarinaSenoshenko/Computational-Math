import unittest

from main import methodGauss, methodYakobi


class MyTestCase(unittest.TestCase):
    def test_Gauss_1(self):
        self.assertEqual(methodGauss([[20, 20, 0, 40], [15, 15, 5, 35], [0, 1, 1, 2]]), [1.0, 1.0, 1.0])

    def test_Gauss_2(self):
        self.assertEqual(methodGauss([[2, 1, -1, 0], [1, -5, 4, 10], [3, 2, 6, 7]]), [1.0, -1.0, 1.0])

    def test_Gauss_3(self):
        self.assertEqual(methodGauss([[5, 1, 0, 1], [1, 5, 1, 1], [0, 1, 5, 1]]), [0.17391304347826086, 0.13043478260869568, 0.17391304347826084])

    def test_Gauss_4(self):
        self.assertEqual(methodGauss([[4, -1, -1, 2], [-1, 4, -1, 2], [-1, -1, 4, 2]]), [1.0, 1.0, 0.9999999999999999])

    def test_Gauss_5(self):
        self.assertEqual(methodGauss([[2, -1, 0, 2], [-1, 2, -1, 2], [0, -1, 2, 2]]), [3.0, 4.0, 2.9999999999999996])

    def test_Gauss_6(self):
        self.assertEqual(methodGauss([[2, 5, 1, 8], [-1, 1.5, 2, 0], [0.5, -8, -5, 7]]), [30.0, -15.764705882352942, 26.823529411764707])

    def test_Yakobi_1(self):
        self.assertEqual(methodYakobi([[2, 1, -1, 0], [1, -5, 4, 10], [3, 2, 6, 7]], 0.000000000000001), [1.0, -0.9999999999999998, 0.9999999999999999])

    def test_Yakobi_2(self):
        self.assertEqual(methodYakobi([[2, 1, -1, 0], [1, -5, 4, 10], [3, 2, 6, 7]], 0.00000001), [0.9999999991447306, -0.9999999997053157, 0.9999999986811836])

    def test_Yakobi_3(self):
        self.assertEqual(methodYakobi([[2, 1, -1, 0], [1, -5, 4, 10], [3, 2, 6, 7]], 0.01), [0.9988344636566703, -1.0018497447033392, 1.0005578665722794])

    def test_Yakobi_4(self):
        self.assertEqual(methodYakobi([[10, 1, -1, 11], [1, 10, -1, 10], [-1, 1, 10, 10]], 0.000000000000001), [1.1020202020202021, 0.9909090909090909, 1.011111111111111])

    def test_Yakobi_5(self):
        self.assertEqual(methodYakobi([[10, 1, -1, 11], [1, 10, -1, 10], [-1, 1, 10, 10]], 0.00000001), [1.102020202, 0.990909091, 1.011111111])

    def test_Yakobi_6(self):
        self.assertEqual(methodYakobi([[10, 1, -1, 11], [1, 10, -1, 10], [-1, 1, 10, 10]], 0.01), [1.102, 0.991, 1.0110000000000001])

    def test_Yakobi_7(self):
        self.assertEqual(methodYakobi([[20, 20, 0, 40], [15, 15, 5, 35], [0, 1, 1, 2]], 0.01), 0)
