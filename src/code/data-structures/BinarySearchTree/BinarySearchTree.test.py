from BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()
assert tree.is_empty() is True
tree.add(1)
assert tree.is_empty() is False

assert tree.size() == 1
tree.remove(1)

assert tree.height() == 0
tree.add('M')
assert tree.height() == 1
tree.add('J')
assert tree.height() == 2
tree.add('S')
assert tree.height() == 2
tree.add('B')
assert tree.height() == 3
tree.add('N')
assert tree.height() == 3
tree.add('Z')
assert tree.height() == 3
tree.add('A')
assert tree.height() == 4

tree.remove('M')
tree.remove('J')
tree.remove('S')
tree.remove('B')
tree.remove('N')
tree.remove('Z')
tree.remove('A')


tree.add('A') is True
tree.add('A') is False
tree.add('B') is True
