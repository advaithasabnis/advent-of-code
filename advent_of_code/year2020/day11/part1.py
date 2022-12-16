from .shared import find_stable_state, parse_map


def main(text):
    data = text.splitlines()
    size = len(data)
    seat_map = parse_map(data)
    seat_map = find_stable_state(seat_map, size, 4, False)
    return sum(seat_map.values())


_input = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()
assert main(_input) == 37
