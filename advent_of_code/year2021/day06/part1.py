from .shared import fish_population


def main(text):
    starting_fish = list(map(int, text.split(',')))
    return fish_population(starting_fish, 80)


_input = """
3,4,3,1,2
""".strip()
assert main(_input) == 5934
