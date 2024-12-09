import math


def convert_digits(quinary: str, mapping: dict[str, str]) -> str:
    """Converts digits in a string using a mapping"""
    converted_string = ''.join(mapping.get(char, char) for char in quinary)
    return converted_string


def geometric_sum(r: int, n: int) -> int:
    return (1 - r**n) // (1 - r)


def decimal_to_quinary(decimal: int) -> str:
    """Converts a decimal number to a quinary number"""
    if decimal == 0:
        return '0'
    result = ''
    while decimal > 0:
        result = str(decimal % 5) + result
        decimal //= 5
    return result


def sum_quinaries(list_of_quinaries: list[str]) -> str:
    # Map to convert digits in the quinary to regular quinary digits that uses digits 0 through 4
    num_map = {'=': '0', '-': '1', '0': '2', '1': '3', '2': '4'}
    inv_map = {v: k for k, v in num_map.items()}

    decimal_sum = 0

    for quinary in list_of_quinaries:
        # Convert to regular quinary digits
        q = convert_digits(quinary, num_map)
        # Convert to decimal and sum
        decimal_sum += int(q, 5)
        # Correct for the conversion to regular quinary digits
        decimal_sum -= 2 * geometric_sum(5, len(q))

    # Find the length of the quinary sum to correct back to the original quinary digits
    len_of_quinary = math.ceil(math.log(decimal_sum, 5))

    # Correct for the conversion to regular quinary digits and convert back to original quinary digits
    quinary_sum = decimal_to_quinary(decimal_sum + 2 * geometric_sum(5, len_of_quinary))
    return convert_digits(quinary_sum, inv_map)


def main(text: str) -> str:
    quinaries = text.splitlines()
    return sum_quinaries(quinaries)


_input = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
""".strip()
assert main(_input) == '2=-1=0'
