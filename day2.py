with open('day2.in') as file:
    strategy = [line.strip().split() for line in file]

ROCK, PAPER, SCISSORS = 'ABC'
WIN, DRAW, LOSE = 6, 3, 0

points = {ROCK: 1, PAPER: 2, SCISSORS: 3}

winchoice = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

mychoice1 = {'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
def outcome1(other, me):
    if me == winchoice[other]:
        return WIN
    if me == other:
        return DRAW
    else:
        return LOSE

def mychoice2(other, outcome):
    if outcome == DRAW:
        return other
    elif outcome == WIN:
        return winchoice[other]
    elif outcome == LOSE:
        return winchoice[winchoice[other]]


outcome2 = {'X': LOSE, 'Y': DRAW, 'Z': WIN}

part1 = sum(
    points[mychoice1[me]] + outcome1(other, mychoice1[me])
    for other, me in strategy
)

part2 = sum(
    points[mychoice2(other, outcome2[me])] + outcome2[me]
    for other, me in strategy
)
print('Part 1:', part1)
print('Part 2:', part2)
