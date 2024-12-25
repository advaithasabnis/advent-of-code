def main(text: str) -> int:
    locks = []
    keys = []
    # For each schematic, convert it to binary and add it to the locks or keys list
    for schematic in text.split('\n\n'):
        # Replace the character '#' with 1 and '.' with 0, then remove the newlines
        s = schematic.replace("#", "1").replace(".", "0").replace("\n", "")
        # If the first character is a 1 (i.e. '#') , it is a lock, otherwise it is a key
        if s[0] == "1":
            locks.append(int(s, 2))
        else:
            keys.append(int(s, 2))

    # For each lock, check if there is a key that can unlock it
    # If the bitwise AND of the lock and key is 0, then the key can unlock the lock
    # because the lock and key have no 1s ('#') in the same position
    return sum(not lock & key for lock in locks for key in keys)


_input = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".strip()

assert main(_input) == 3
