import re


def main(text: str) -> int:
    block_pattern = re.compile(r"(?:do\(\)|^)(.*?)(?:don't\(\)|$)", re.DOTALL)

    # Extract blocks between "do()" or start and "don't()" or end
    blocks = block_pattern.findall(text)

    # Regex for capturing `mul(...)` within extracted blocks
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    # Find all `mul(...)` in valid blocks
    matches = []
    for block in blocks:
        matches.extend(mul_pattern.findall(block))

    result = sum(int(m[0]) * int(m[1]) for m in matches)

    return result


_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
assert main(_input) == 48
