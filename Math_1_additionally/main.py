from params import *
from view import Visualizer
from runte_curt_fourth_order import ApproximationWithFourthOrder
from euler_with_recalculation import ApproximationWithSecondOrder

H = 1 / N

class Controller(object):
    def __init__(self):
        self.approximator1 = ApproximationWithSecondOrder(H, N)
        self.approximator2 = ApproximationWithFourthOrder(H, N)

        printResult(self.approximator1, self.approximator2)

        self.approximator3 = ApproximationWithSecondOrder(H / 2, 2 * N)
        self.approximator4 = ApproximationWithFourthOrder(H / 2, 2 * N)

        rungeCheck(self.approximator1, self.approximator3, 2)
        rungeCheck(self.approximator2, self.approximator4, 4)

        self.visualiser = Visualizer(self.approximator2.x_array, self.approximator1.y_array, self.approximator2.y_array)
        self.visualiser.showApproximationGraphic()


Controller()
