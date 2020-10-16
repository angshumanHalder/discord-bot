from IndexedPriorityQueue import IndexedPriorityQueue

pq = IndexedPriorityQueue(7)

pq.insert(4, 4)
assert pq.contains(4) is True
assert pq.peek_min_value() == 4
assert pq.peek_min_key_idx() == 4

pq.update(4, 8)
assert pq.peek_min_value() == 8
assert pq.poll_min_key_idx() == 4
assert pq.contains(4) is False

pq.insert(3, 99)
pq.insert(1, 101)
pq.insert(2, 60)
assert pq.peek_min_value() == 60
assert pq.peek_min_key_idx() == 2
pq.increase_key(2, 150)
assert pq.peek_min_value() == 99
assert pq.peek_min_key_idx() == 3
pq.increase_key(3, 250)
assert pq.peek_min_value() == 101
assert pq.peek_min_key_idx() == 1
pq.decrease_key(3, -500)
assert pq.peek_min_value() == -500
assert pq.peek_min_key_idx() == 3
assert pq.contains(3) is True
pq.delete(3)
assert pq.contains(3) is False
assert pq.peek_min_value() == 101
assert pq.peek_min_key_idx() == 1
assert pq.value_of(1) == 101
