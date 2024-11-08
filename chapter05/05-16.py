import itertools
items = ['a', 'b', 'c', 'd']

print(list(map(''.join, itertools.permutations(items))))