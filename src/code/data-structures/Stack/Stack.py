# Using array

class Stack:
    def __init__(self):
        self.__size = 0
        self.__data = []

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def push(self, val):
        self.__data.append(val)
        self.__size += 1

    def pop(self):
        if self.is_empty():
            return ValueError('Stack is empty')
        self.__size -= 1
        return self.__data.pop()

    def peek(self):
        if self.is_empty():
            return ValueError('Stack is empty')
        return self.__data[-1]
