from PriorityQueue import PriorityQueue

que = PriorityQueue()
assert que.size() == 0
assert que.is_empty() is True
assert que.peek() is None
assert que.poll() is None


def add_to_heap():
    que.add(3, 3)
    que.add(2, 2)
    que.add(5, 5)
    que.add(6, 6)
    que.add(7, 7)
    que.add(9, 9)
    que.add(4, 4)
    que.add(8, 8)
    que.add(1, 1)


add_to_heap()
for i in range(1, 10):
    assert que.poll().value == i

que.clear()
assert que.size() == 0

add_to_heap()
assert que.contains(3) is True
assert que.contains(4) is True
assert que.contains(2) is True
assert que.contains(11) is False
assert que.contains(12) is False
assert que.contains(9) is True
