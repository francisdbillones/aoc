def main():
    with open("input.txt") as reader:
        lines = reader.read().splitlines()

    games = [tuple(line.split()) for line in lines]
    games = [(c1, {'X': 'A', 'Y': 'B', 'Z': 'C'}[c2]) for c1, c2 in games]
    print(part1(games))
    print(part2(games))

def part1(games):
    return sum(
        won(c2, c1) + {'A': 1, 'B': 2, 'C': 3}[c2] for c1, c2 in games
    )

def part2(games):
    return sum(
       {'A': 0, 'B': 3, 'C': 6}[c2] + score({'A': lose(c1), 'B': c1, 'C': win(c1)}[c2]) for c1, c2 in games
    )

def win(pick):
    return {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }[pick]

def lose(pick):
    return {
        'A': 'C',
        'B': 'A',
        'C': 'B',
    }[pick]

def score(pick):
    return {'A': 1, 'B': 2, 'C': 3}[pick]

def won(c1, c2):
    if c1 == c2:
        return 3 
    return {
        ('A', 'B'): 0,
        ('A', 'C'): 6,
        ('B', 'A'): 6,
        ('B', 'C'): 0,
        ('C', 'A'): 0,
        ('C', 'B'): 6,
    }[c1, c2]

if __name__ == "__main__":
    main()
