import statistics


def main(text):
    positions = list(map(int, text.split(',')))
    # The geometric median is the point that minimizes the sum of
    # distances to the sample points. For 1-D, the median is the
    # geometric median
    # https://en.wikipedia.org/wiki/Geometric_median
    opt_position = int(statistics.median(positions))
    return sum([abs(n - opt_position) for n in positions])


_input = """
16,1,2,0,4,2,7,1,2,14
""".strip()
assert main(_input) == 37
