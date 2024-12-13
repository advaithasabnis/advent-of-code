import re
from typing import NamedTuple


class Machine(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int
    X: int
    Y: int


def parse_text(text: str) -> list[Machine]:
    """Parse the text into a list of Machines."""
    pattern = re.compile(r"^.*?: X[\+\=](\d+), Y[\+\=](\d+)$", re.MULTILINE)

    data = text.split("\n\n")
    machines = []
    for line in data:
        match = pattern.findall(line)
        machines.append(Machine(*map(int, [i for j in match for i in j])))

    return machines
