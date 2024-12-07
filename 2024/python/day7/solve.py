from math import log10, floor


def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    part1(lines)
    part2(lines)


def part1(lines):
    equations = []

    for line in lines:
        answer, equation = line.split(": ")
        equation = int(answer), tuple(map(int, equation.split()))
        equations.append(equation)

    print(sum(solve_eq(equation) or 0 for equation in equations))


def part2(lines):
    equations = []

    for line in lines:
        answer, equation = line.split(": ")
        equation = int(answer), tuple(map(int, equation.split()))
        equations.append(equation)

    print(
        sum(
            solve_eq(equation, enable_concat=True) or 0
            for equation in equations
        )
    )


def solve_eq(equation, enable_concat=False):
    answer, equation = equation

    if len(equation) == 1:
        return answer if equation[0] == answer else None
    rest, last_term = equation[:-1], equation[-1]

    if (
        solve_eq(
            (answer - last_term, rest),
            enable_concat=enable_concat,
        )
        is not None
    ):
        return answer

    if (
        answer % last_term == 0
        and solve_eq(
            (answer // last_term, rest),
            enable_concat=enable_concat,
        )
        is not None
    ):
        return answer

    if (
        enable_concat
        and answer % (10 ** floor(log10(last_term) + 1)) == last_term
        and solve_eq(
            ((answer - last_term) // (10 ** floor(log10(last_term) + 1)), rest),
            enable_concat=enable_concat,
        )
        is not None
    ):
        return answer
    return None


if __name__ == "__main__":
    main()
