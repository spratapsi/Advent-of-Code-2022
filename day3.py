from string import ascii_letters
import more_itertools as mi

rucksacks = []
with open('day3.in') as file:
    for line in file:
        line = line.strip()
        left = set(line[:len(line) // 2])
        right = set(line[len(line) // 2:])
        rucksacks.append([left, right])

priority = {letter: p for p, letter in enumerate(ascii_letters, 1)}
repeated_types = [left & right for left, right in rucksacks]
part1 = sum(priority[t] for types in repeated_types for t in types)

common_types = [
    ((a1 | a2) &  (b1 | b2) &  (c1 | c2)).pop()
    for (a1, a2), (b1, b2), (c1, c2) in mi.grouper(rucksacks, 3)
]
part2 = sum(priority[t] for t in common_types)

print('Part 1:', part1)
print('Part 2:', part2)
