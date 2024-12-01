def main():
    with open("input.txt") as reader:
        lines = reader.read().splitlines()

    print(part1(lines))
    print(part2(lines))

def part1(sacks):
    return sum(
        priority(next(iter(set.intersection(*map(set, split(sack))))))
        for sack in sacks
    )

def part2(sacks):
    return sum(
        priority(next(iter(set.intersection(*map(set, chunk)))))
        for chunk in chunks(sacks, 3)
    )

def chunks(sacks, size):
    return (sacks[i:i + size] for i in range(0, len(sacks), size))


def priority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    elif char.isupper():
        return ord(char) - ord('A') + 27

def split(sack):
    l = len(sack)

    return sack[:l//2], sack[l//2:]

if __name__ == "__main__":
    main()
