class PriorityQueue:
    class _Node:
        def __init__(self, value, priority):
            self.value = value
            self.priority = priority

        def __str__(self):
            return (
                " { val: " + str(self.value) + ", priority: " + str(self.priority) + "}"
            )

    def __init__(self):
        self.heap = []

    def clear(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def contains(self, element):
        for ele in self.heap:
            if ele.value == element:
                return True
        return False

    def add(self, element, priority):
        if element is None or priority is None:
            raise ValueError("Element or Priority cannnot be None")
        node = self._Node(element, priority)
        self.heap.append(node)
        index_of_last_element = len(self.heap) - 1
        self._swim(index_of_last_element)

    def _less(self, i, j):
        return self.heap[i].priority <= self.heap[j].priority

    def _swim(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self._less(idx, parent):
            self._swap(parent, idx)
            idx = parent
            parent = (idx - 1) // 2

    def _sink(self, idx):
        heap_size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left
            if right < heap_size and self._less(right, left):
                smallest = right

            if left >= heap_size or self._less(idx, smallest):
                break

            self._swap(smallest, idx)
            idx = smallest

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def remove(self, element):
        if not self.contains(element):
            return False
        for i, h_val in enumerate(self.heap):
            if element == h_val.value:
                self.removeAt(i)
                return True
        return False

    def removeAt(self, idx):
        if self.is_empty():
            return None
        last_idx = self.size() - 1
        remove_data = self.heap[idx]
        self._swap(idx, last_idx)
        self.heap.pop(last_idx)

        if idx == last_idx:
            return remove_data
        element = self.heap[idx]

        self._sink(idx)

        if self.heap[idx] == element:
            self._swim(idx)
        return remove_data

    def isMinHeap(self, k=0):
        heap_size = self.size()
        if k >= heap_size:
            return True

        left = 2 * k + 1
        right = 2 * k + 2

        if left < heap_size and not self._less(k, left):
            return False
        if right < heap_size and not self._less(k, right):
            return False
        return self.isMinHeap(left) and self.isMinHeap(right)

    def __str__(self):
        lst_str = ""
        for n in self.heap:
            lst_str += str(n) + ","
        return lst_str