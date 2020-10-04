class DoublyLinkedList:
    """ Private Node Class """
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

        def __str__(self):
            return self.value

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
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def push_end(self, value):
        node = self._Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def push_at_index(self, value, index):
        if self._is_empty():
            raise IndexError("List is empty")
        self._is_out_of_bounds(index)

        if index == 0:
            self.push_beginning(value)
        if index >= self.length - 1:
            self.push_end(value)
        else:
            node = self._Node(value)
            i = 0
            temp_node = self.head
            while i < index - 1:
                temp_node = temp_node.next
                i += 1
            node.next = temp_node.next
            temp_node.next.prev = node
            node.prev = temp_node
            temp_node.next = node
        self.length += 1
        return True

    def remove_beginning(self):
        if self._is_empty():
            raise IndexError("List is empty")

        value = self.head.value
        self.head = self.head.next
        self.head.prev.next = None
        self.head.prev = None
        self.length -= 1
        return value

    def remove_end(self):
        if self._is_empty():
            raise IndexError("List is empty")

        value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next.prev = None
        self.tail.next = None
        self.length -= 1
        return value

    def remove_at_index(self, index):
        if self._is_empty():
            raise IndexError("List is empty")
        self._is_out_of_bounds(index)
        
        if index == 0:
            self.remove_beginning()
        if index >= self.length - 1:
            self.remove_end()
        else:
            i = 0
            temp_node = self.head
            while i < index - 1:
                temp_node = temp_node.next
                i += 1
            node_remove = temp_node.next
            value = node_remove.value
            temp_node.next = node_remove.next
            node_remove.next = None
            temp_node.next.prev = temp_node
            node_remove.prev = None
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
        temp_node_head = self.head
        temp_node_tail = self.tail
        i = 0
        while i < int(self.length / 2):
            temp_value = temp_node_tail.value
            temp_node_tail.value = temp_node_head.value
            temp_node_head.value = temp_value
            temp_node_tail = temp_node_tail.prev
            temp_node_head = temp_node_head.next
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
  