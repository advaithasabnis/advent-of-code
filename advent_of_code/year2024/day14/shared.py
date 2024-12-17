import re


def parse_input(text: str) -> list[tuple[int, int, int, int]]:
    data = text.splitlines()
    pattern = re.compile(r"p\=(-?\d+),(-?\d+) v\=(-?\d+),(-?\d+)")
    robots = []
    for robot in data:
        x, y, vx, vy = map(int, pattern.findall(robot)[0])
        robots.append((x, y, vx, vy))
    return robots


def sign(x: int, limit: int) -> int:
    return (x > limit) - (x < limit)
