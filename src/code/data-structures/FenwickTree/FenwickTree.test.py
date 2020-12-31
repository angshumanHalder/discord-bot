from FenwickTree import (
  FenwickTreeRangeQueryAndPointUpdate,
  FenwickTreeRangeUpdateAndPointQuery
)


#  Range query and point update test

lst = [None, 1, 2, 3, 4, 5, 6]
ft = FenwickTreeRangeQueryAndPointUpdate(lst)

assert ft.sum(1, 6) == 21
assert ft.sum(1, 5) == 15
assert ft.sum(1, 4) == 10
assert ft.sum(1, 3) == 6
assert ft.sum(1, 2) == 3
assert ft.sum(1, 1) == 1

assert ft.sum(3, 4) == 7
assert ft.sum(2, 6) == 20
assert ft.sum(4, 5) == 9
assert ft.sum(6, 6) == 6
assert ft.sum(5, 5) == 5
assert ft.sum(4, 4) == 4
assert ft.sum(3, 3) == 3
assert ft.sum(2, 2) == 2
assert ft.sum(1, 1) == 1


lst = [None, -1, -2, -3, -4, -5, -6]
ft = FenwickTreeRangeQueryAndPointUpdate(lst)

assert ft.sum(1, 6) == -21
assert ft.sum(1, 5) == -15
assert ft.sum(1, 4) == -10
assert ft.sum(1, 3) == -6
assert ft.sum(1, 2) == -3
assert ft.sum(1, 1) == -1

assert ft.sum(6, 6) == -6
assert ft.sum(5, 5) == -5
assert ft.sum(4, 4) == -4
assert ft.sum(3, 3) == -3
assert ft.sum(2, 2) == -2
assert ft.sum(1, 1) == -1


# Range update and point query test
values = [None, 2, 3, 4, 5, 6]
ftr = FenwickTreeRangeUpdateAndPointQuery(values)
ftr.updateRange(2, 4, 10)

assert ftr.get(1) == 2
assert ftr.get(2) == 13
assert ftr.get(3) == 14
assert ftr.get(4) == 15
assert ftr.get(5) == 6


values = [None, 2, -3, -4, 5, 6]
ftr = FenwickTreeRangeUpdateAndPointQuery(values)
ftr.updateRange(2, 4, 10)

assert ftr.get(1) == 2
assert ftr.get(2) == 7
assert ftr.get(3) == 6
assert ftr.get(4) == 15
assert ftr.get(5) == 6
