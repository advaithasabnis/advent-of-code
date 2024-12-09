from typing import cast


Position = tuple[int, int, int]


def neighbors(pos: Position) -> set[Position]:
    x, y, z = pos
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    }


def main(text: str) -> int:
    cubes = cast(set[Position], {tuple(map(int, l.split(','))) for l in text.splitlines()})
    return sum((s not in cubes) for c in cubes for s in neighbors(c))
