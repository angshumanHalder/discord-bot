from UnionFind import UnionFind

unionFind = UnionFind(5)
assert unionFind.components() == 5
unionFind.unify(0, 1)
assert unionFind.components() == 4
unionFind.unify(1, 0)
assert unionFind.components() == 4
unionFind.unify(1, 2)
assert unionFind.components() == 3
unionFind.unify(0, 2)
assert unionFind.components() == 3
unionFind.unify(2, 1)
assert unionFind.components() == 3
unionFind.unify(3, 4)
assert unionFind.components() == 2
unionFind.unify(4, 3)
assert unionFind.components() == 2
unionFind.unify(1, 3)
assert unionFind.components() == 1
unionFind.unify(4, 0)
assert unionFind.components() == 1
