def main():
    with open("input.txt") as reader:
        lines = reader.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    part1(lines)
    part2(lines)

def radiating_xmases(lines, i, j):
    return lines[i][j] == "X" and \
            (j >= 3 and lines[i][j-3:j+1][::-1] == "XMAS") + \
            (j <= len(lines[0]) - 4 and lines[i][j:j+4] == "XMAS") + \
            (i >= 3 and "".join(lines[i-k][j] for k in range(4)) == "XMAS") + \
            (i <= len(lines) - 4 and "".join(lines[i+k][j] for k in range(4)) == "XMAS") + \
            (i >= 3 and j >= 3 and "".join(lines[i-k][j-k] for k in range(4)) == "XMAS") + \
            (i <= len(lines) - 4 and j <= len(lines[0]) - 4 and "".join(lines[i+k][j+k] for k in range(4)) == "XMAS") + \
            (i >= 3 and j <= len(lines[0]) - 4 and "".join(lines[i-k][j+k] for k in range(4)) == "XMAS") + \
            (i <= len(lines) - 4 and j >= 3 and "".join(lines[i+k][j-k] for k in range(4)) == "XMAS")

def radiating_mases(lines, i, j):
    return lines[i][j] == "A" and \
            (lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]) in ("MAS", "SAM") and \
            (lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1]) in ("MAS", "SAM")

def part1(lines):
    rows, cols = len(lines), len(lines[0])
    count = sum(radiating_xmases(lines, i, j) for i in range(rows) for j in range(cols))
    print(count)

def part2(lines):
    rows, cols = len(lines), len(lines[0])
    count = sum(radiating_mases(lines, i, j) for i in range(1, rows-1) for j in range(1, cols-1))
    print(count)

if __name__ == "__main__":
    main()
