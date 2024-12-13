from collections import deque


def main(text: str) -> int:
    data = list(map(int, text))
    files = data[::2]

    file_blocks: deque[int] = deque()
    for idx, size in enumerate(files):
        for _ in range(size):
            file_blocks.append(idx)

    compact = []

    for idx, size in enumerate(data):
        c = 0
        if idx % 2 == 0:
            while c < size and file_blocks:
                compact.append(file_blocks.popleft())
                c += 1
        else:
            while c < size and file_blocks:
                compact.append(file_blocks.pop())
                c += 1

    checksum = 0
    for idx, n in enumerate(compact):
        checksum += idx * n

    return checksum


assert main('2333133121414131402') == 1928
