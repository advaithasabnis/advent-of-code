import re


def main(text: str) -> int:
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = mul_pattern.findall(text)

    result = sum(int(m[0]) * int(m[1]) for m in matches)

    return result


_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
assert main(_input) == 161
