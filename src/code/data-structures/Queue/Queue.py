class Queue:
    def __init__(self):
        self.__data = []

    def enqueue(self, val):
        self.__data.append(val)

    def dequeue(self):
        if self.is_empty():
            return ValueError('Queue is empty')
        return self.__data.pop(0)

    def peek(self):
        return self.__data[0]

    def size(self):
        return len(self.__data)

    def is_empty(self):
        return len(self.__data) == 0
