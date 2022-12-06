import re
from collections import namedtuple
from copy import deepcopy

stacks = []
instructions = []
with open('day5.in') as file:
    for line in file:
        if not line.strip():
            break
        stacks.append(line.rstrip()[1::4])
    stacks = [list(''.join(reversed(col)).rstrip()) for col in zip(*stacks)]

    template_instruction = re.compile(r'move (\d+) from (\d) to (\d)')
    for line in file:
        m = re.match(template_instruction, line.rstrip())
        if m:
            instructions.append([int(x) for x in m.groups()])

def move(stacks, instructions, reverse=True):
    stacks = deepcopy(stacks)
    for qty, source, target in instructions:
        to_move = stacks[source-1][-1:-qty-1:-1]
        stacks[target-1] += to_move if reverse else to_move[::-1]
        del stacks[source-1][-1:-qty-1:-1]
    return stacks

stacks1 = move(stacks, instructions, reverse=True)
part1 = ''.join(stack[-1] if stack else '' for stack in stacks1)

stacks2 = move(stacks, instructions, reverse=False)
part2 = ''.join(stack[-1] if stack else '' for stack in stacks2)


print('Part 1:', part1)
print('Part 2:', part2)
