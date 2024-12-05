def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    empty_line_index = lines.index("-")
    rules, updates = lines[:empty_line_index], lines[empty_line_index + 1 :]

    rules = {tuple(map(int, rule.split("|"))) for rule in rules}
    updates = [list(map(int, update.split(","))) for update in updates]

    part1(rules.copy(), updates.copy())
    part2(rules.copy(), updates.copy())


def part1(rules, updates):
    print(
        sum(
            update[len(update) // 2]
            for update in updates
            if valid_update(update, rules)
        )
    )


def part2(rules, updates):
    print(
        sum(
            sort_pages(update, rules)[len(update) // 2]
            for update in updates
            if not valid_update(update, rules)
        )
    )


def valid_update(update, rules):
    return all(greater(b, a, rules) for a, b in zip(update[:-1], update[1:]))


def greater(a, b, rules):
    return (b, a) in rules


def sort_pages(pages, rules):
    from functools import cmp_to_key

    return sorted(
        pages, key=cmp_to_key(lambda a, b: 1 if greater(a, b, rules) else -1)
    )


if __name__ == "__main__":
    main()
