import time
import view
from approximator import CauchyTaskApproximator

A = 10
N = 1000_000
H = 2 * A / N


class Controller(object):
    def __init__(self):
        self.approximator = CauchyTaskApproximator(A, N, H)

        start = time.perf_counter()
        self.approximator.countApproximation()
        appr_time = time.perf_counter() - start

        start = time.perf_counter()
        self.approximator.findDiscrepancy()
        discrepancy_time = time.perf_counter() - start

        start = time.perf_counter()
        # self.approximator.printResult()
        print_res_time = time.perf_counter() - start

        self.visualiser = view.CauchyTaskVisualizer(self.approximator.x_array,
                                                    self.approximator.y_array,
                                                    self.approximator.a)
        self.visualiser.showApproximationGraphic()

        print("Approximation time: {0} sec".format(appr_time))
        print("Count discrepancy time: {0} sec".format(discrepancy_time))
        print("Print table time: {0} sec".format(print_res_time))


Controller()
