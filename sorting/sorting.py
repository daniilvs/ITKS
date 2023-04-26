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


class Sort:

    def bubble(self: list) -> list:
        size = len(self)
        swapped = False
        for _iter in range(size - 1):
            for j in range(_iter):
                swapped = True
                if self[j] > self[j + 1]:
                    self[j], self[j + 1] = self[j + 1], self[j]
            if not swapped:
                return self
        return self

    def insertion(self: list) -> list:
        size = len(self)
        for i in range(1, size):
            key = self[i]
            j = i - 1
            while j >= 0 and key < self[j]:
                self[j + 1] = self[j]
                j -= 1
            self[j + 1] = key
        return self

    def selection(self: list) -> list:
        size = len(self)
        for i in range(size):
            lowest = i
            for j in range(i + 1, size):
                if self[j] < self[lowest]:
                    lowest = j
                self[i], self[lowest] = self[lowest], self[i]
        return self

    def merge(self: list) -> list:
        size = len(self)
        if size > 1:
            mid = size // 2
            left = self[:mid]
            right = self[mid:]
            left.merge()
            right.merge()
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    self[k] = left[i]
                    i += 1
                else:
                    self[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self[k] = right[j]
                j += 1
                k += 1
        return self
