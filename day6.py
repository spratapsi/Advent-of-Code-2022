with open('day6.in') as file:
    signal = file.read().strip()

def first_unique(signal, k):
    for i in range(len(signal)):
        if len(set(signal[i:i+k])) == k:
            return i + k

part1 = first_unique(signal, 4)
part2 = first_unique(signal, 14)

print('Part 1:', part1)
print('Part 2:', part2)
