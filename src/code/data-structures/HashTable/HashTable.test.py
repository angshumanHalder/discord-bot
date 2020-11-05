""" This file will contains different hashtable test cases """

# HashTable separate chaining test case
from HashTable import HashTableSeparateChaining

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
