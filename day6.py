import itertools as it

with open('day6.in') as file:
    signal = next(iter(file)).strip()

def first_unique(signal, k):
    for i in it.count():
        characters = set(signal[i:i+k])
        if len(characters) == k:
            return i + k

part1 = first_unique(signal, 4)
part2 = first_unique(signal, 14)

print('Part 1:', part1)
print('Part 2:', part2)
