from .shared import DumboGrid


def main(text):
    grid = DumboGrid(text)
    return grid.find_sync_step()


_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".strip()
assert main(_input) == 195
