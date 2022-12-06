import re
from copy import deepcopy

stacks = []
instructions = []
with open('day5.in') as file:
    for line in file:
        if not line.strip():
            break
        stacks.append(line[1::4])
    stacks = [list(''.join(reversed(col)).rstrip()) for col in zip(*stacks)]

    for line in file:
        match = re.match(r'move (\d+) from (\d) to (\d)', line.rstrip())
        if match:
            instructions.append([int(x) for x in match.groups()])

def move(stacks, instructions, reverse=True):
    stacks = deepcopy(stacks)
    for ncrates, source, target in instructions:
        to_move = stacks[source-1][-1:-ncrates-1:-1]
        stacks[target-1] += to_move if reverse else to_move[::-1]
        del stacks[source-1][-1:-ncrates-1:-1]
    return stacks

stacks1 = move(stacks, instructions, reverse=True)
part1 = ''.join(stack[-1] if stack else '' for stack in stacks1)

stacks2 = move(stacks, instructions, reverse=False)
part2 = ''.join(stack[-1] if stack else '' for stack in stacks2)

print('Part 1:', part1)
print('Part 2:', part2)
