A = {1,2,3,4}
B = {5,6,7,4}

A = frozenset([1,2,3,4])
B = frozenset([5,6,7,4])

print(A.isdisjoint(B))

print(A.difference(B))

print(A|B)

frozenset({1,2,3,4,5,6})


