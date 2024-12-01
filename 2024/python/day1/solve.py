def main():
    with open("input.txt") as reader:
        lines = reader.readlines()

    part1(lines)
    part2(lines)

def part1(lines):
    pairs = [tuple(map(int, line.split())) for line in lines if line.strip()]

    first_list = sorted([a for a, _ in pairs])
    second_list = sorted([b for _, b in pairs])

    ans = sum(abs(a - b) for a, b in zip(first_list, second_list))
    print(ans)

def part2(lines):
    pairs = [tuple(map(int, line.split())) for line in lines if line.strip()]

    first_list = [a for a, _ in pairs]
    second_list = [b for _, b in pairs]

    from collections import Counter
    
    second_list_counter = Counter(second_list)

    similarity = sum(k * second_list_counter[k] for k in first_list)
    print(similarity)

if __name__ == "__main__": main()
