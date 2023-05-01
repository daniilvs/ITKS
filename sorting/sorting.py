import time
import numpy as np

NUMBER_OF_ITERS = {
    100: 1000,
    1000: 1000,
    # 10000: 100,
    # 100000: 100,
    # 1000000: 10
}

SIZE_OF_ARRAY = list(NUMBER_OF_ITERS.keys())

CLOCKS = {
    100: 0.0,
    1000: 0.0,
    10000: 0.0,
    100000: 0.0,
    1000000: 0.0
}


def bubble(arr: list) -> list:
    size = len(arr)
    swapped = False
    for _iter in range(size - 1, 0, -1):
        for j in range(_iter):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return arr
    return arr


def insertion(arr: list) -> list:
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection(arr: list) -> list:
    size = len(arr)
    for i in range(size):
        lowest = i
        for j in range(i + 1, size):
            if arr[j] < arr[lowest]:
                lowest = j
            arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


def merge(arr: list) -> list:
    size = len(arr)
    if size > 1:
        mid = size // 2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def heapify(arr: list, size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < size and arr[root] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, size, largest)


def heap(arr: list) -> list:
    size = len(arr)
    for i in range(size // 2, -1, -1):
        heapify(arr, size, i)
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def quick(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick(left) + [pivot] + quick(right)


def counting(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
    return arr


def radix(arr: list) -> list:
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        counting(arr, exp)
        exp *= 10
    return arr


def create(number, percent_of_sorted=0):
    if percent_of_sorted != 0:
        almost = number - number // 10
        presorted = quick(list(np.random.sample(almost)))
        return list(np.random.sample(number // 10)).append(presorted)
    else:
        return list(np.random.sample(number))


def time_of_sort(sorting_algorithm):
    average_clocks = CLOCKS.copy()
    for n in SIZE_OF_ARRAY:
        clocks = []
        for i in range(NUMBER_OF_ITERS[n]):
            arr = create(n)
            start_time = time.time()
            sorting_algorithm(arr)
            end_time = time.time() - start_time
            clocks.append(end_time)
        average_clocks[n] = sum(clocks) / NUMBER_OF_ITERS[n]
    print(average_clocks)


if __name__ == '__main__':
    print(quick(create(10, True)))
    time_of_sort(quick)
