def main():
    with open("input.txt") as reader:
        lines = reader.readlines()

    part1(lines)

def part1(lines):
    instructions = [line.split() for line in lines]
    instructions = [(direction, int(magnitude)) for direction, magnitude in instructions]
    
    visited = [[0] *  ex]
    
    print(instructions)

if __name__ == "__main__":
    main()
