from .shared import Pos, shortest_path


def find_critical_blocker(blockers: list[Pos], first_N: int, dimensions: int) -> Pos | None:
    """Binary search to find the first critical blocker that makes a path impossible."""
    left, right = first_N, len(blockers)
    while left < right:
        mid = (left + right) // 2
        current_blockers = set(blockers[: mid + 1])
        if shortest_path(current_blockers, dimensions) == -1:
            right = mid
        else:
            left = mid + 1
    return blockers[left] if left < len(blockers) else None


def main(text: str, first_N: int = 1024, dimensions: int = 71) -> str:
    blockers: list[Pos] = []
    for line in text.splitlines():
        x, y = map(int, line.split(','))
        blockers.append((x, y))

    critical_blocker = find_critical_blocker(blockers, first_N, dimensions)

    if critical_blocker is None:
        return 'Could not find critical blocker'

    return f'{critical_blocker[0]},{critical_blocker[1]}'


_input = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()

assert main(_input, 12, 7) == "6,1"
