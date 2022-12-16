from .shared import Rule, optimize_rules, parse_notes


def is_valid_field(n, rule: Rule):
    return (n >= rule.l1 and n <= rule.u1) or (n >= rule.l2 and n <= rule.u2)


def main(text):
    rules, my_ticket, nearby_tickets = parse_notes(text)
    optimized_rules = optimize_rules(rules)

    # Get valid tickets
    valid_tickets = []
    for i, ticket in enumerate(nearby_tickets):
        for item in ticket:
            for lower, upper in optimized_rules:
                if item >= lower and item <= upper:
                    break
            else:
                break
        else:
            valid_tickets.append(ticket)
    # Add your ticket to valids
    valid_tickets.append(my_ticket)

    # Get possible index to field mappings
    possibilities = {}
    for rule in rules:
        possibilities[rule.field] = [
            i
            for i in range(len(rules))
            if all([is_valid_field(t[i], rule) for t in valid_tickets])
        ]

    # Get exact index to field mapping by elimination
    matches = {}
    possibilities = sorted(possibilities.items(), key=lambda x: len(x[1]))
    for field, possible_indices in possibilities:
        index = [i for i in possible_indices if i not in matches]
        assert len(index) == 1
        matches[index[0]] = field

    # Calculate product of fields with "departure" in the name
    prod = 1
    for i, field in matches.items():
        if 'departure' in field:
            prod *= my_ticket[i]
    return prod


_input = """
departure class: 0-1 or 4-19
departure row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
3,9,18
15,1,5
5,14,9
""".strip()
assert main(_input) == 132
