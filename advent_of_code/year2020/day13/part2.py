from functools import reduce


# Bus numbers are co prime and we can use Chinese remainder theorem
# Using modular multiplicative inverse (https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)
def crt_solution(buses):
    r, b = zip(*buses)
    value = 0
    for i in range(len(b)):
        m = reduce(lambda x, y: x * y, b) // b[i]
        value += r[i] * m * pow(m, -1, b[i])
    return value % reduce(lambda x, y: x * y, b)


def main(text):
    data = text.splitlines()[1]
    buses = [
        (int(bus) - offset, int(bus)) for offset, bus in enumerate(data.split(',')) if bus != 'x'
    ]
    return crt_solution(buses)


_input = """
939
7,13,x,x,59,x,31,19
""".strip()
assert main(_input) == 1068781
