from sys import argv


def main():
    if "test" in argv:
        input_file = "test_input.txt"
    else:
        input_file = "input.txt"

    with open(input_file) as reader:
        input = reader.read()
        print("part1:")
        # part1(input)

        print("part2:")
        part2(input)


def part1(text):
    lines = [line for line in text.split("\n") if line]

    s = 0
    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]
        s += 10 * digits[0] + digits[-1]

    print(s)


def part2(text):
    lines = [line for line in text.split("\n") if line]

    digit_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    s = 0
    for line in lines:
        first = find_first_digit(line, digit_dict)
        last = find_last_digit(line, digit_dict)
        s += first * 10 + last

    print(s)


def find_first_digit(line, digit_dict):
    for i, c in enumerate(line):
        if c.isdigit():
            return int(c)
        for digit_name, digit in digit_dict.items():
            substr = line[i : i + len(digit_name)]
            if substr == digit_name:
                return digit


def find_last_digit(line, digit_dict):
    for i in reversed(range(len(line))):
        c = line[i]
        if c.isdigit():
            return int(c)
        for digit_name, digit in digit_dict.items():
            substr = line[i - len(digit_name) + 1 : i + 1]
            if substr == digit_name:
                return digit


if __name__ == "__main__":
    main()
