def find_trees(text: str, right: int, down: int) -> int:
    data = text.splitlines()
    count = 0
    width = len(data[0])
    pos = right
    for i in data[down::down]:
        if i[pos % width] == '#':
            count += 1
        pos += right
    return count