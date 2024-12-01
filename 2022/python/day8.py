import numpy as np

def main():
    with open("input.txt") as reader:
        lines = reader.read().splitlines()

    mat = [[int(c) for c in line] for line in lines]
    mat = np.array(mat)

    print(part1(mat))
    print(part2(mat))


def part1(mat):
    h, w = mat.shape

    visible = (h * 2) + (w * 2) - 4 # all edges

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            visible += is_visible(mat, i, j)

    return visible

def part2(mat):
    h, w = mat.shape

    return max(scenic_score(mat, i, j) for i in range(h) for j in range(w))

def scenic_score(mat, i, j):
    val = mat[i, j]

    left = mat[i, :j][::-1]
    right = mat[i, j+1:]
    top = mat[:i, j][::-1]
    bot = mat[i+1:, j]

    score = 1
    for line in (left, right, top, bot):
        score *= viewing_distance(val, line)

    return score

def viewing_distance(val, line):
    if not line.shape[0]:
        return 0
    ar = line >= val
    if ar.any():
        return np.nonzero(ar)[0][0] + 1
    else:
        return line.shape[0]

def is_visible(mat, i, j):
    val = mat[i, j]

    left = mat[i, :j]
    right = mat[i,j+1:]
    top = mat[:i, j]
    bot = mat[i+1:, j]

    if val > left.max() \
        or val > right.max() \
        or val > top.max() \
        or val > bot.max():
        return True
    else:
        return False


if __name__ == "__main__":
    main()
