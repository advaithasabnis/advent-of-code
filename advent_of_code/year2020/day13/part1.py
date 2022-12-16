def find_best_bus(t, buses):
    times = [b - t % b for b in buses]
    t_next_bus = min(times)
    return t_next_bus * buses[times.index(t_next_bus)]


def main(text):
    data = text.splitlines()
    t = int(data[0])
    buses = [int(x) for x in data[1].split(',') if x != 'x']
    return find_best_bus(t, buses)


_input = """
939
7,13,x,x,59,x,31,19
""".strip()
assert main(_input) == 295
