from collections import defaultdict
from itertools import accumulate


def calculate_dir_sizes(text: str) -> dict[str, int]:
    # Initialize a variable to hold total directory sizes
    dirs: dict[str, int] = defaultdict(int)

    # Initialize a variable to hold the current path as a list of directories
    curr = ['/']

    # Process each line
    for line in text.splitlines():
        match line.split():
            case '$', 'cd', '/':
                curr = ['/']
            case '$', 'cd', '..':
                curr.pop()
            case '$', 'cd', x:
                curr.append(x + '/')
            case '$', 'ls':
                pass
            case 'dir', _:
                pass
            case size, _:
                # Add size to current directory and all parents
                # https://docs.python.org/3/library/itertools.html#itertools.accumulate
                for p in accumulate(curr):
                    dirs[p] += int(size)

    return dirs
