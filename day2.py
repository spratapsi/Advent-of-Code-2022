with open('day2.in') as file:
    strategy = [line.strip().split() for line in file]

ROCK, PAPER, SCISSORS = 0, 1, 2
DRAW, WIN, LOSE = 0, 1, 2

def points(my_hand, outcome):
    points_hand = {ROCK: 1, PAPER: 2, SCISSORS: 3}
    points_outcome = {LOSE: 0, DRAW: 3, WIN: 6}
    return points_hand[my_hand] + points_outcome[outcome] 

def points1(input_a, input_b):
    my_hand = 'XYZ'.index(input_b)
    other_hand = 'ABC'.index(input_a)
    outcome = (my_hand - other_hand) % 3
    return points(my_hand, outcome)

def points2(input_a, input_b):
    outcome = {'X': LOSE, 'Y': DRAW, 'Z': WIN}[input_b]
    other_hand = 'ABC'.index(input_a)
    my_hand = (other_hand + outcome) % 3
    return points(my_hand, outcome)

part1 = sum(points1(input_a, input_b) for input_a, input_b in strategy)
part2 = sum(points2(input_a, input_b) for input_a, input_b in strategy)

print('Part 1:', part1)
print('Part 2:', part2)
