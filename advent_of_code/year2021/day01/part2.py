from .shared import measure


def main(text):
    return measure(text, 3)


_input = """
199
200
208
210
200
207
240
269
260
263
""".strip()
assert main(_input) == 5
