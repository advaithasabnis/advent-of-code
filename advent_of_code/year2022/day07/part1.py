from .shared import calculate_dir_sizes


def main(text: str) -> int:
    dirs = calculate_dir_sizes(text)
    return sum(s for s in dirs.values() if s <= 100_000)


_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()
assert main(_input) == 95437
