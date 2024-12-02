def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]
    part1(lines)
    part2(lines)

def part1(lines):
    nums = [list(map(int, line.split())) for line in lines]

    print(sum(safe(report) for report in nums))

def safe(report):
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]

    for diff1, diff2 in zip(diffs[:-1], diffs[1:]):
        if diff1 * diff2 < 0:
            return False
        if not (1 <= abs(diff1) <= 3):
            return False
        if not (1 <= abs(diff2) <= 3):
            return False
    return True

def part2(lines):
    nums = [list(map(int, line.split())) for line in lines]

    print(sum(safe2(report) for report in nums))

def safe2(report):
    for i, level in enumerate(report):
        report.pop(i)
        if safe(report):
            return True
        report.insert(i, level)
    return False


if __name__ == "__main__":
    main()
