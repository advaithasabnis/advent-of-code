def find_next_number(x: int) -> int:
    x = x ^ (x << 6) & 0xFFFFFF
    x = x ^ (x >> 5)  # Mask isn't needed here
    x = x ^ (x << 11) & 0xFFFFFF
    return x


def find_nth_number(x: int, n: int) -> int:
    for _ in range(n):
        x = find_next_number(x)
    return x


def main(text: str) -> int:
    total = 0
    for line in text.splitlines():
        x = int(line)
        total += find_nth_number(x, 2000)

    return total


_input = """
1
10
100
2024
""".strip()

assert main(_input) == 37327623
