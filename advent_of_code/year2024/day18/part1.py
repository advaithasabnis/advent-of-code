from .shared import Pos, shortest_path


def main(text: str, first_N: int = 1024, dimensions: int = 71) -> int:
    blockers: set[Pos] = set()
    for line in text.splitlines()[:first_N]:
        x, y = map(int, line.split(','))
        blockers.add((x, y))

    return shortest_path(blockers, dimensions)


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

assert main(_input, 12, 7) == 22
