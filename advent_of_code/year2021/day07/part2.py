import statistics


def main(text):
    positions = list(map(int, text.split(',')))
    # If d is the distance between a point 'x' and optimal position 'p'
    # i.e. d = abs(x - p), we need to minimze f(p) = SUM[d(d+1)/2]
    # This is a convex function differentiable at d!=0
    # f(p) is minimum when f'(p) = 0 and f'(p) is bounded at d=0
    # The real minimum for f(p) is when p is between mean - 0.5 and mean + 0.5
    mean = int(statistics.mean(positions))
    opt_position_range = range(mean - 1, mean + 2)
    fuel_amounts = []
    for opt_position in opt_position_range:
        fuel = 0
        for n in positions:
            distance = abs(n - opt_position)
            fuel += (distance * (distance + 1)) / 2
        fuel_amounts.append(fuel)

    return int(min(fuel_amounts))


_input = """
16,1,2,0,4,2,7,1,2,14
""".strip()
assert main(_input) == 168
