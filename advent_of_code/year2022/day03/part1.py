from string import ascii_letters


def main(text: str) -> int:
    bags = text.splitlines()
    sum_priority = 0
    for bag in bags:
        c1, c2 = set(bag[: len(bag) // 2]), set(bag[len(bag) // 2 :])
        (item,) = c1 & c2
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
