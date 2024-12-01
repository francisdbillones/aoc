def main():
    with open("input.txt") as reader:
        lines = reader.read().splitlines()

    pairs = []
    
    for line in lines:
        s1, s2 = line.split(',')
        p1 = tuple(map(int, s1.split('-')))
        p2 = tuple(map(int, s2.split('-')))
        pairs.append((p1, p2))

    print(part1(pairs))
    print(part2(pairs))

def part1(pairs):
    n = 0

    for p1, p2 in pairs:
        p11, p12 = p1
        p21, p22 = p2

        if p11 <= p21 and p22 <= p12:
            n += 1
        elif p21 <= p11 and p12 <= p22:
            n += 1

    return n

def part2(pairs):
    n = 0

    for p1, p2 in pairs:
        p11, p12 = p1
        p21, p22 = p2

        if p21 < p11:
            p11, p21 = p21, p11
            p12, p22 = p22, p12

        if p21 <= p12:
            n += 1

    return n
    
if __name__ == "__main__":
    main()
