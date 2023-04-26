from sorting import NUMBER_OF_ITERS, SIZE_OF_ARRAY, CLOCKS, Arr
import time
import numpy as np


def create(number, half_sorted=False):
    if half_sorted:
        presorted = [i for i in range(0.0, 1.0, 0.000001)]
        return np.random.sample(number // 10).append(presorted)
    else:
        return np.random.sample(number)


def time_of_sort(sorting_algorithm: Arr):
    average_clocks = CLOCKS.copy()
    for n in SIZE_OF_ARRAY:
        clocks = []
        for i in range(NUMBER_OF_ITERS[n]):
            start_time = time.time()
            arr = Arr(n)
            sorting_algorithm(arr)
            end_time = time.time() - start_time
            clocks.append(end_time)
        average_clocks[n] = sum(clocks) / NUMBER_OF_ITERS[n]
    print(average_clocks)


if __name__ == '__main__':

    time_of_sort(arr.Arr.bubble())