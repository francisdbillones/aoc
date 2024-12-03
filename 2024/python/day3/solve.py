def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    raw_input = "".join(lines)

    part1(raw_input)
    part2(raw_input)

def part1(raw_input):
    print(sum(parse_muls(raw_input)))

def parse_muls(line):
    import re
    numbers = re.findall(r'mul\((\d+),(\d+)\)', line)
    return [int(a) * int(b) for a, b in numbers]

def part2(raw_input):
    print(sum(parse_muls2(raw_input)))

def parse_muls2(line):
    import re
    line = re.sub(r'don\'t\(\).*?do\(\)', '', line)
    line = re.sub(r'don\'t\(\).*$', '', line)
    numbers = re.findall(r'mul\((\d+),(\d+)\)', line)
    return [int(a) * int(b) for a, b in numbers]

if __name__ == "__main__":
    main()
