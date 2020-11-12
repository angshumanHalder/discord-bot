""" This file will contains different hashtable test cases """

from HashTable import HashTableSeparateChaining, HashTableLinearProbing, HashTableQuadraticProbing

# HashTable separate chaining test case
hash_table = HashTableSeparateChaining()

hash_table.add(1, 1)
assert hash_table.get(1) == 1
hash_table.add(1, 5)
assert hash_table.get(1) == 5
hash_table.add(1, -7)
assert hash_table.get(1) == -7

hash_table.put(11, 0)
hash_table.put(12, 0)
hash_table.put(13, 0)
assert hash_table.size() == 4

for i in range(1, 11):
    hash_table.put(i, 0)
assert hash_table.size() == 13

for i in range(1, 11):
    hash_table.remove(i)
assert hash_table.size() == 3


# Linear Probing test case
lp_hash_table = HashTableLinearProbing(6, 0.9)

lp_hash_table.add(1, 1)
assert lp_hash_table.get(1) == 1
lp_hash_table.add(1, 5)
assert lp_hash_table.get(1) == 5
lp_hash_table.add(1, -7)
assert lp_hash_table.get(1) == -7
lp_hash_table.put(11, 0)
lp_hash_table.put(12, 0)
lp_hash_table.put(13, 0)
assert lp_hash_table.size() == 4
for i in range(1, 11):
    lp_hash_table.put(i, 0)
assert lp_hash_table.size() == 13


for i in range(1, 11):
    lp_hash_table.remove(i)
assert lp_hash_table.size() == 3


# Quadratic Probing test case
qp_hash_table = HashTableQuadraticProbing(6, 0.9)
qp_hash_table.add(1, 1)
assert qp_hash_table.get(1) == 1
qp_hash_table.add(1, 5)
assert qp_hash_table.get(1) == 5
qp_hash_table.add(1, -7)
assert qp_hash_table.get(1) == -7
qp_hash_table.put(11, 0)
qp_hash_table.put(12, 0)
qp_hash_table.put(13, 0)
assert qp_hash_table.size() == 4
for i in range(1, 11):
    qp_hash_table.put(i, 0)
assert qp_hash_table.size() == 13


for i in range(1, 11):
    qp_hash_table.remove(i)
assert qp_hash_table.size() == 3
