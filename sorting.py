import time
import prettytable
import numpy as np

NUMBER_OF_ITERS = {
    100: 1000,
    1000: 1000,
    10000: 100,
    100000: 100,
    1000000: 10
}

CLOCKS = {
    100: 0.0,
    1000: 0.0,
    10000: 0.0,
    100000: 0.0,
    1000000: 0.0
}


class Arr:
    def __init__(self, number):
        self.ls: list = np.random.sample(number)
        self.size = len(self.ls)

    def bubble(self) -> list:
        swapped = False
        for _iter in range(self.size - 1, 0, -1):
            for j in range(_iter):
                swapped = True
                if self.ls[j] > self.ls[j + 1]:
                    self.ls[j], self.ls[j + 1] = self.ls[j + 1], self.ls[j]
            if not swapped:
                return self.ls
        return self.ls

    def insertion(self):
        return


if __name__ == '__main__':
    num = list(NUMBER_OF_ITERS.keys())
    average_clocks = CLOCKS.copy()
    for n in num:
        clocks = []
        for i in range(NUMBER_OF_ITERS[n]):
            start_time = time.time()
            Arr(n).bubble()
            end_time = time.time() - start_time
            clocks.append(end_time)
        average_clocks[n] = sum(clocks) / NUMBER_OF_ITERS[n]
    print(average_clocks)



