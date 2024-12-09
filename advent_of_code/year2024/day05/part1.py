from .shared import Graph


def main(text: str) -> int:
    rules, updates = text.split('\n\n')

    graph = Graph(rules)

    updates_list = [list(map(int, l.split(','))) for l in updates.splitlines()]

    return sum(lst[len(lst) // 2] for lst in updates_list if graph.is_valid(lst))


_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75, 47, 61, 53, 29
97, 61, 53, 29, 13
75, 29, 13
75, 97, 47, 61, 53
61, 13, 29
97, 13, 75, 29, 47
""".strip()


assert main(_input) == 143
