with open("day1.in") as f:
    calories = [0]
    for line in f:
        if line.strip():
            calories[-1] += int(line) 
        else:
            calories.append(0)

calories.sort()

print('Part 1:', calories[-1])
print('Part 2:', sum(calories[-3:]))
