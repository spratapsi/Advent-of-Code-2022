from dataclasses import dataclass

@dataclass
class Interval:
    lo: int
    hi: int

    def __contains__(self, other):
        return self.lo <= other.lo and other.hi <= self.hi

    def __and__(self, other):
        return Interval(max(self.lo, other.lo,), min(self.hi, other.hi))

    def __bool__(self):
        return self.lo <= self.hi

pairs = []
with open('day4.in') as file:
    for line in file:
        (a, b), (c, d) = [x.split('-') for x in line.strip().split(',')]
        first = Interval(int(a), int(b))
        second = Interval(int(c), int(d))
        pairs.append((first, second))

part1 = sum(a in b or b in a for a, b in pairs)
part2 = sum(bool(a & b) for a, b in pairs)

print('Part 1:', part1)
print('Part 2:', part2)
