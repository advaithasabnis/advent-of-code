def parse_calories(text: str) -> list:
    data = text.split('\n\n')
    calrories = []
    for row in data:
        calrories.append(sum([int(x) for x in row.split()]))
    return calrories
