from typing import Final


# Fenwick Tree range query and point update
class FenwickTreeRangeQueryAndPointUpdate:
    # Construct a Fenwick Tree with an initial set of values.
    # The values must be one based meaning values[0] won't get used
    def __init__(self, values):
        if not values:
            raise ValueError('Values array cannot be None')
        self.N: Final = len(values)
        values[0] = 0

        # Make a clone of the original values array since we are going to manipulate the array
        self.tree = values.copy()
        for i in range(1, self.N):
            parent = i + self.__lsb(i)
            if parent < self.N:
                self.tree[parent] += self.tree[i]

    # Returns the least significant bit
    def __lsb(self, i):
        return i & -i

    # Computes the prefix sum from [1, i], O(log(n))
    def __prefix_sum(self, i):
        total = 0
        while i != 0:
            total += self.tree[i]
            i &= ~self.__lsb(i)
        return total

    # Returns the sum of the interval [left, right], O(log(n))
    def sum(self, left, right):
        if right < left:
            raise ValueError('Make sure right >= left')
        return self.__prefix_sum(right) - self.__prefix_sum(left - 1)

    # Get value at index i
    def get(self, i):
        return self.sum(i, i)

    # Add 'v' to index i
    def __add(self, i, v):
        while i < self.N:
            self.tree[i] += v
            i += self.__lsb(i)

    # Set index i to be equal to v, O(long(n))
    def set(self, i, v):
        self.__add(i, v - self.sum(i, i))

    def __repr__(self):
        return self.tree


# Fenwick Tree range update and point query
class FenwickTreeRangeUpdateAndPointQuery:
    def __init__(self, values):
        if not values:
            raise ValueError('Values array cannot be None')
        self.N: Final = len(values)
        values[0] = 0

        # Make a clone of the original values array since we are going to manipulate the array
        self.tree = values.copy()
        for i in range(1, self.N):
            parent = i + self.__lsb(i)
            if parent < self.N:
                self.tree[parent] += self.tree[i]

        self.originalTree = self.tree
        self.currentTree = self.tree.copy()

    # Update the interval [left, right] with the value 'val', O(log(n))
    def updateRange(self, left, right, val):
        self.__add(left, +val)
        self.__add(right + 1, -val)

    # Add 'v' to index 'i' and all the ranges responsible for 'i', O(log(n))
    def __add(self, i, v):
        while i < self.N:
            self.currentTree[i] += v
            i += self.__lsb(i)

    # Get the value at a specific index. The logic behind this method is the
    # same as finding the prefix sum in a Fenwick tree except that you need to
    # take the difference between the current tree and the original to get
    # the point value.
    def get(self, i):
        return self.__prefix_sum(i, self.currentTree) - self.__prefix_sum(i - 1, self.originalTree)

    # Computes the prefix sum from [1, i], O(log(n))
    def __prefix_sum(self, i, tree):
        total = 0
        while i != 0:
            total += tree[i]
            i &= ~self.__lsb(i)
        return total

    def __lsb(self, i):
        return i & -i
