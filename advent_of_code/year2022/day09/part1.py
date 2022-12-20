def sign(x: float) -> int:
    return (x > 0) - (x < 0)


def main(text: str) -> int:
    # Represent positions of head and tail in complex coordinates
    # Initial position is 0+0j for both head and tail
    h, t = 0 + 0j, 0 + 0j
    move = {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}

    # Initialize variable to hold coordinates visited by tail
    visited = {0 + 0j}

    # Parse the motions of the head
    motions = [(m.split()) for m in text.splitlines()]

    for direction, distance in motions:
        d = int(distance)
        for _ in range(d):
            h += move[direction]
            delta = h - t
            # Tail moves towards head if it is >=2 units away
            if abs(delta) >= 2:
                t += complex(sign(delta.real), sign(delta.imag))
                visited.add(t)

    return len(visited)


_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()
assert main(_input) == 13
