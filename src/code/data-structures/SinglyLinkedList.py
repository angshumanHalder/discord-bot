# Node class
class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

# Linked List Class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_beginning(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def push_end(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def push_at_index(self, value, index):
        if index == 0:
            self.push_beginning(value)
        elif index >= self.length - 1:
            self.push_end(value)
        else:
            node = Node(value)
            i = 0
            temp_node = self.head
            while i < index - 1:
                temp_node = temp_node.next
                i += 1
            node.next = temp_node.next
            temp_node.next = node
            self.length += 1

    def remove_beginning(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None
        self.length -= 1
        return value

    def remove_end(self):
        if self.length == 0:
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
        if self.length == 0:
            raise IndexError("List is empty")
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
        if self.length == 0:
            raise IndexError("List is empty")
        if index >= self.length:
            raise IndexError(f"No node at index {index}")
        i = 0
        temp_node = self.head
        while i < index:
            temp_node = temp_node.next
            i += 1
        return temp_node.value

    def set_value_at(self, value, index):
        if self.length == 0:
            raise IndexError("List is empty")
        if index >= self.length:
            raise IndexError(f"No node at index {index}")
        i = 0
        temp_node = self.head
        while i < index:
            temp_node = temp_node.next
            i += 1
        temp_node.value = value

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

    def __str__(self):
        temp_node = self.head
        lst_str = ""
        while temp_node is not None:
            lst_str += str(temp_node.value) + ", "
            temp_node = temp_node.next
        return lst_str
  