from string import ascii_letters


def main(text: str) -> int:
    bags = text.splitlines()
    sum_priority = 0
    # Iterate over list of bags, 3 bags at a time
    for bag1, bag2, bag3 in zip(*[iter(bags)] * 3):
        (item,) = set(bag1) & set(bag2) & set(bag3)
        sum_priority += ascii_letters.index(item) + 1
    return sum_priority


_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()
assert main(_input) == 70
