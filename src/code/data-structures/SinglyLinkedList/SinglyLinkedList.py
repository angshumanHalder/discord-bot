# Linked List Class
class SinglyLinkedList:
    """ Private Node Class """
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_beginning(self, value):
        node = self._Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def push_end(self, value):
        node = self._Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def push_at_index(self, value, index):
        if self._is_empty() and index != 0:
            raise IndexError("List is empty")
        self._is_out_of_bounds(index)

        if index == 0:
            self.push_beginning(value)
        elif index >= self.length - 1:
            self.push_end(value)
        else:
            node = self._Node(value)
            i = 0
            temp_node = self.head
            while i < index - 1:
                temp_node = temp_node.next
                i += 1
            node.next = temp_node.next
            temp_node.next = node
            self.length += 1
            return True

    def remove_beginning(self):
        if self._is_empty():
            raise IndexError("List is empty")

        value = self.head.value
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        self.length -= 1
        return value

    def remove_end(self):
        if self._is_empty():
            raise IndexError("List is empty")

        value = self.tail.value
        temp_node = self.head
        while temp_node.next.next is not None:
            temp_node = temp_node.next
        self.tail = temp_node
        self.tail.next = None
        self.length -= 1
        return value

    def remove_at_index(self, index):
        if self._is_empty():
            raise IndexError("List is empty")
        self._is_out_of_bounds(index)

        if index == 0:
            value = self.remove_beginning()
        elif index >= self.length - 1:
            value - self.remove_end()
        else:
            i = 0
            temp_node = self.head
            while i < index - 1:
                temp_node = temp_node.next
                i += 1
            node_remove = temp_node.next
            value = node_remove.value
            temp_node.next = temp_node.next.next
            node_remove.next = None
        self.length -= 1
        return value

    def get_value_at(self, index):
        if self._is_empty():
            raise IndexError("List is empty")
        self._is_out_of_bounds(index)

        i = 0
        temp_node = self.head
        while i < index:
            temp_node = temp_node.next
            i += 1
        return temp_node.value

    def set_value_at(self, value, index):
        if self._is_empty():
            raise IndexError("List is empty")
        self._is_out_of_bounds(index)

        i = 0
        temp_node = self.head
        while i < index:
            temp_node = temp_node.next
            i += 1
        temp_node.value = value
        return True

    def reverse_list(self):
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node
        prev_node = None
        next_node = None
        i = 0
        while i < self.length:
            next_node = temp_node.next
            temp_node.next = prev_node
            prev_node = temp_node
            temp_node = next_node
            i += 1
        return True

    """ Helper methods """

    def size(self):
        return self.length

    def _is_empty(self):
        return self.length == 0

    def _is_out_of_bounds(self, idx):
        if idx >= self.length:
            raise IndexError('Index out of bounds')

    def __str__(self):
        temp_node = self.head
        lst_str = "["
        while temp_node is not None:
            lst_str += str(temp_node.value)
            if temp_node.next is not None:
                lst_str += ","
            temp_node = temp_node.next
        lst_str += "]"
        return lst_str
