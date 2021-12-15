from .shared import cave_system


def main(text):
    caves = cave_system(text)
    all_paths = caves.find_all_paths(part2=True)
    return len(all_paths)


_input = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip()
assert main(_input) == 103
