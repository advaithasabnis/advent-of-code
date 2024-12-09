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

    # Find the bounds of the space
    min_values = [min(c[i] for c in cubes) - 1 for i in range(3)]
    max_values = [max(c[i] for c in cubes) + 1 for i in range(3)]

    todo = cast(list[Position], [tuple(min_values)])
    seen = set(todo)

    # Perform 3D flood-fill operation and then calculate the surface area
    while todo:
        here = todo.pop()
        # Neighbors within the bounds of the space and not already seen and not part of cubes
        new = [
            s
            for s in (neighbors(here) - cubes - seen)
            if all(m <= c <= n for m, c, n in zip(min_values, s, max_values))
        ]
        # Add valid neighors to continue flood-fill on
        todo += new
        # Since these are already in todo, they can be marked as seen
        seen |= set(new)

    return sum((s in seen) for c in cubes for s in neighbors(c))
