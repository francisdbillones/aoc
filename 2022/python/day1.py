def main():
    with open("input.txt") as reader:
        lines = reader.read().splitlines()

    chunks = []
    current_chunk = []

    for line in lines:
        if line == '':
            chunks.append(current_chunk)
            current_chunk = []
        else:
            current_chunk.append(int(line))

    top_3 = sorted([sum(chunk) for chunk in chunks])[-3:]
    print(top_3)
    print(sum(top_3))

if __name__ == "__main__":
    main()
