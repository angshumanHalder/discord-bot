from Queue import Queue

queue = Queue()
assert queue.is_empty() is True
queue.enqueue(1)
assert queue.is_empty() is False
queue.enqueue(2)
assert queue.size() == 2
assert queue.peek() == 1
assert queue.size() == 2
assert queue.dequeue() == 1
assert queue.size() == 1
assert queue.peek() == 2
assert queue.size() == 1
assert queue.dequeue() == 2
assert queue.size() == 0
assert queue.is_empty() is True
