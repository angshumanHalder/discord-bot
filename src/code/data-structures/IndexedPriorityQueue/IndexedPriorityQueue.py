"""
# Storing the values
# Each index represent a unique key (key = index)
# Each index which will represent the key will have the value associated with it

# Storing the position of the key index
# Each index represent unique key
# Each index will store the position of the unique key

# Storing the key-index
# Each index will represent the position
# Each index will store the key at that position
"""


class IndexedPriorityQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.values = [-1] * self.max_size
        self.position_map = [-1] * self.max_size
        self.inverse_map = [-1] * self.max_size
        self.sz = 0

    def size(self):
        return self.sz

    def is_empty(self):
        return self.sz == 0

    def contains(self, key_idx):
        if key_idx < 0 or key_idx >= self.max_size:
            raise IndexError('Index out of bounds')
        return self.position_map[key_idx] != -1

    def delete(self, key_idx):
        if not self.contains(key_idx):
            raise ValueError("Key does not exists")

        i = self.position_map[key_idx]
        self.sz -= 1
        self.__swap(i, self.sz)
        self.__sink(i)
        self.__swim(i)
        val = self.values[key_idx]
        self.values[key_idx] = -1
        self.position_map[key_idx] = -1
        self.inverse_map[self.sz] = -1
        return val

    def value_of(self, key_idx):
        if not self.contains(key_idx):
            raise ValueError("Key does not exists")
        return self.values[key_idx]

    def poll_min_key_idx(self):
        min_key = self.peek_min_key_idx()
        self.delete(min_key)
        return min_key

    def peek_min_key_idx(self):
        if self.is_empty():
            raise ValueError("Element does not exists")
        return self.inverse_map[0]

    def peek_min_value(self):
        if self.is_empty():
            raise ValueError("Element does not exists")
        return self.values[self.inverse_map[0]]

    def poll_min_value(self):
        min_value = self.peek_min_value()
        self.delete(self.peek_min_key_idx())
        return min_value

    def insert(self, key_idx, value):
        if value is None:
            raise ValueError("Value cannot be None")
        if self.contains(key_idx):
            raise IndexError("Value already exists")

        self.position_map[key_idx] = self.sz
        self.inverse_map[self.sz] = key_idx
        self.values[key_idx] = value
        self.__swim(self.sz)
        self.sz += 1

    def update(self, key_idx, value):
        if value is None:
            raise ValueError("Value cannot be None")
        if not self.contains(key_idx):
            raise IndexError("Key does not exists")

        i = self.position_map[key_idx]
        old_value = self.values[key_idx]
        self.values[key_idx] = value
        self.__swim(i)
        self.__sink(i)
        return old_value

    def decrease_key(self, key_idx, value):
        if value < self.values[key_idx]:
            self.values[key_idx] = value
            self.__swim(self.position_map[key_idx])

    def increase_key(self, key_idx, value):
        if value > self.values[key_idx]:
            self.values[key_idx] = value
            self.__sink(self.position_map[key_idx])

    def __sink(self, i):
        j = self.__min_child(i)
        while j != -1:
            self.__swap(i, j)
            i = j
            j = self.__min_child(i)

    def __swim(self, i):
        parent = i // 2
        while parent >= 0 and self.__is_less(i, parent):
            self.__swap(parent, i)
            i = parent
            parent = i // 2

    def __swap(self, i, j):
        self.position_map[self.inverse_map[j]] = i
        self.position_map[self.inverse_map[i]] = j
        self.inverse_map[i], self.inverse_map[j] = self.inverse_map[j], self.inverse_map[i]

    def __is_less(self, i, j):
        return (
            self.values[self.inverse_map[i]] < self.values[self.inverse_map[j]]
        ) and (
            self.values[self.inverse_map[i]] != -
            1 and self.values[self.inverse_map[j]] != -1
        )

    def __min_child(self, i):
        idx = -1
        __from = i * 2 + 1
        to = min(self.sz, __from + 2)
        for j in range(__from, to):
            if self.__is_less(j, i):
                idx = i = j
        return idx

    def __repr__(self):
        for i in range(len(self.values)):
            print(self.values[i], self.position_map[i], self.inverse_map[i])
        return ""
