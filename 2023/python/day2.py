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
    ...


def part2(text):
    ...


if __name__ == "__main__":
    main()
