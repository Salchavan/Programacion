from itertools import product

alphabet = 'abcdefghijklmnñopqrstuvwxyz'
combinations = [''.join(i) for i in product(alphabet, repeat = 3)]

print(combinations)
print(len(combinations))