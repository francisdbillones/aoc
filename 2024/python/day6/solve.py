def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    part1(lines)
    part2(lines)


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def part1(lines):
    grid = [[{".": 0, "#": 1, "^": 2}[c] for c in line] for line in lines]
    guard = [
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == 2
    ][0]
    print(guard_area(grid, guard, UP) + 1)


def guard_area(grid, guard, direction):
    area = 0
    h, w = len(grid), len(grid[0])
    grid = [row.copy() for row in grid]
    while True:
        guard = (guard[0] + direction[0], guard[1] + direction[1])
        if not (0 <= guard[0] < h and 0 <= guard[1] < w):
            return area
        if grid[guard[0]][guard[1]] == 0:
            area += 1
        elif grid[guard[0]][guard[1]] == 1:
            # undo move
            guard = (guard[0] - direction[0], guard[1] - direction[1])
            new_direction = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}[
                direction
            ]
            return area + guard_area(grid, guard, new_direction)
        grid[guard[0]][guard[1]] = -1
    return area


def advance_state(guard, grid, direction):
    h, w = len(grid), len(grid[0])
    while True:
        guard = (guard[0] + direction[0], guard[1] + direction[1])
        if not (0 <= guard[0] < h and 0 <= guard[1] < w):
            return None  # guard escaped

        if grid[guard[0]][guard[1]] == 1:
            # undo move
            guard = (guard[0] - direction[0], guard[1] - direction[1])
            new_direction = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}[
                direction
            ]
            return (guard, grid, new_direction)


def part2(lines):
    grid = [[{".": 0, "#": 1, "^": 2}[c] for c in line] for line in lines]
    guard = [
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == 2
    ][0]

    empty = [
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == 0
    ]

    new_states = []
    for (i, j) in empty:
        new_grid = [row.copy() for row in grid]
        new_grid[i][j] = 1
        new_states.append((guard, new_grid, UP))

    count = 0
    len_new_states = len(new_states)
    print(len(new_states))
    while True:
        for i, state in enumerate(new_states):
            if state is None:
                continue
            if (state := advance_state(*state)) is None:
                count += 1
                print(len_new_states - count)
            new_states[i] = state


if __name__ == "__main__":
    main()
