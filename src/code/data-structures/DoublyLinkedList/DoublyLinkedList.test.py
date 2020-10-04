from DoublyLinkedList import DoublyLinkedList

linkedList = DoublyLinkedList()
assert linkedList.push_beginning(1) is True
assert linkedList.push_beginning(2) is True
assert linkedList.push_end(3) is True
assert linkedList.push_end(4) is True
assert linkedList.push_end(5) is True
assert linkedList.push_at_index(80, 3) is True
assert linkedList.__str__() == "[2,1,3,80,4,5]"
assert linkedList.remove_beginning() == 2
assert linkedList.__str__() == "[1,3,80,4,5]"
assert linkedList.remove_end() == 5
assert linkedList.remove_at_index(2) == 80
assert linkedList.get_value_at(2) == 4
assert linkedList.set_value_at(20, 0) is True
assert linkedList.__str__() == "[20,3,4]"
assert linkedList.push_end(40) is True
assert linkedList.__str__() == "[20,3,4,40]"
assert linkedList.reverse_list() is True
assert linkedList.__str__() == "[40,4,3,20]"
