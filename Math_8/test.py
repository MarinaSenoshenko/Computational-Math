import unittest

from main import trapezoidMethod, errorRateTrapezoidMethod, threeEightMethod, errorRateThreeEightMethod


class MyTestCase(unittest.TestCase):
    def test_trapezoidMethod_1(self):
        self.assertEqual('{:.1f}'.format(trapezoidMethod(0, 2, 9)), '11.0')

    def test_trapezoidMethod_2(self):
        self.assertEqual('{:.2f}'.format(trapezoidMethod(0, 2, 210)), '10.67')

    def test_trapezoidMethod_3(self):
        self.assertEqual('{:.5f}'.format(trapezoidMethod(0, 2, 2100)), '10.66667')

    def test_threeEightMethod_1(self):
        self.assertEqual('{:.2f}'.format(threeEightMethod(0, 2, 9)), '10.67')

    def test_threeEightMethod_2(self):
        self.assertEqual('{:.7f}'.format(threeEightMethod(0, 2, 210)), '10.6666667')

    def test_threeEightMethod_3(self):
        self.assertEqual('{:.11f}'.format(threeEightMethod(0, 2, 2100)), '10.66666666667')

    def test_errorRateTrapezoidMethod_1(self):
        self.assertEqual(errorRateTrapezoidMethod(0, 2, 9), 1.31687242798354)

    def test_errorRateTrapezoidMethod_2(self):
        self.assertEqual(errorRateTrapezoidMethod(0, 2, 210), 0.0024187452758881152)

    def test_errorRateTrapezoidMethod_3(self):
        self.assertEqual(errorRateTrapezoidMethod(0, 2, 2100), 2.4187452758883862e-05)

    def test_errorRateThreeEightMethod_1(self):
        self.assertEqual(errorRateThreeEightMethod(0, 2, 9), 0.0048773052888279236)

    def test_errorRateThreeEightMethod_2(self):
        self.assertEqual(errorRateThreeEightMethod(0, 2, 210), 7.051735498216114e-10)

    def test_errorRateThreeEightMethod_3(self):
        self.assertEqual(errorRateThreeEightMethod(0, 2, 2100), 7.051735498216377e-15)
