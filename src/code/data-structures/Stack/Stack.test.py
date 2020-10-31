from Stack import Stack

stack = Stack()
assert stack.is_empty() is True
stack.push(1)
assert stack.is_empty() is False
stack.push(2)
assert stack.size() == 2
assert stack.peek() == 2
assert stack.size() == 2
assert stack.pop() == 2
assert stack.size() == 1
assert stack.peek() == 1
assert stack.size() == 1
assert stack.pop() == 1
assert stack.size() == 0
assert stack.is_empty() is True
