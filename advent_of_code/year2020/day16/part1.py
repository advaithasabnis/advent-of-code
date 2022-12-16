from .shared import optimize_rules, parse_notes


def main(text):
    rules, _, nearby_tickets = parse_notes(text)
    optimized_rules = optimize_rules(rules)
    error_rate = 0
    for ticket in nearby_tickets:
        for item in ticket:
            for lower, upper in optimized_rules:
                if item >= lower and item <= upper:
                    break
            else:
                error_rate += item

    return error_rate


_input = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip()
assert main(_input) == 71
