import itertools as it


def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    part1(lines)
    part2(lines)


def get_antennas(lines):
    antennas = {}

    h, w = len(lines), len(lines[0])
    for i, j in it.product(range(h), range(w)):
        c = lines[i][j]
        if c != ".":
            antennas.setdefault(c, []).append((i, j))
    return antennas


def part1(lines):
    h, w = len(lines), len(lines[0])

    antennas = get_antennas(lines)

    antinodes = set()

    for k in antennas:
        for p1, p2 in it.combinations(antennas[k], 2):
            p1, p2 = sorted((p1, p2), key=lambda x: x[0])

            m = (p2[0] - p1[0], p2[1] - p1[1])

            for antinode in (
                (p1[0] - m[0], p1[1] - m[1]),
                (p2[0] + m[0], p2[1] + m[1]),
            ):
                if 0 <= antinode[0] < h and 0 <= antinode[1] < w:
                    antinodes.add(antinode)
    print(len(antinodes))


def part2(lines):
    h, w = len(lines), len(lines[0])

    antennas = get_antennas(lines)

    antinodes = set()

    for k in antennas:
        for p1, p2 in it.combinations(antennas[k], 2):
            p1, p2 = sorted((p1, p2), key=lambda x: x[0])

            m = (p2[0] - p1[0], p2[1] - p1[1])

            for s in (1, -1):
                for i in it.count():
                    antinode = (
                        p1[0] + i * m[0] * s,
                        p1[1] + i * m[1] * s,
                    )
                    if 0 <= antinode[0] < h and 0 <= antinode[1] < w:
                        antinodes.add(antinode)
                    else:
                        break

    print(len(antinodes))


if __name__ == "__main__":
    main()
