from __future__ import annotations

from dataclasses import dataclass

@dataclass
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    items: list[Directory | File]
    parent: Directory | None

    def size(self) -> int:
        return sum(file.size for file in self.subfiles()) \
            + sum(subdir.size() for subdir in self.subdirs())

    def subdirs(self):
        return (child for child in self.items if isinstance(child, Directory))

    def subfiles(self):
        return (child for child in self.items if isinstance(child, File))

def main():
    with open("input.txt") as reader:
        lines = reader.read().splitlines()

    root = build_directory(lines)

    print(part1(root))
    print(part2(root))

def part1(root):
    over_100k = 0 

    if root.size() <= 100_000:
        over_100k += root.size()
    for subdir in root.subdirs():
        over_100k += part1(subdir) 

    return over_100k

def part2(root):
    capacity = 70_000_000
    require = 30_000_000
    used = root.size()
    unused = capacity - used
    needed = require - unused

    nodes = nested_subdirs(root)
    nodes = [node for node in nodes if node.size() > needed]
    return min(nodes, key=lambda node: node.size() - needed).size()

def nested_subdirs(node):
    ret = [*node.subdirs()]
    for subdir in node.subdirs():
        ret.extend(nested_subdirs(subdir))

    return ret

def build_directory(lines):
    text = '\n'.join(lines)
    chunks = text.split('$ cd ')

    root = Directory(name='/', items=[], parent=None)
    cursor = root

    for chunk in chunks:
        # breakpoint()
        chunk_lines = chunk.splitlines()
        if not chunk_lines:
            continue
        cd_to = chunk_lines[0]
        if cd_to == '/':
            root = Directory(name='/', items=[], parent=None)
            cursor = root
        else:
            for subdir in cursor.subdirs():
                if subdir.name == cd_to:
                    cursor = subdir
        for i, line in enumerate(chunk_lines):
            if line == '..':
                cursor = cursor.parent
            elif line == '$ ls':
                for line in chunk_lines[i + 1:]:
                    size_or_type, name = line.split()
                    if size_or_type == 'dir':
                        child = Directory(name=name, items=[], parent=cursor)
                    else:
                        child = File(name=name, size=int(size_or_type)) 
                    cursor.items.append(child)
                break
    return root

    

if __name__ == "__main__":
    main()
