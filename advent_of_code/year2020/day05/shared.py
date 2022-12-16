import math


def get_row_id(text: str) -> int:
    min_row = 0
    max_row = 127
    for char in text[:7]:
        if char == "F":
            max_row = math.floor((min_row + max_row) / 2)
        elif char == "B":
            min_row = math.ceil((min_row + max_row) / 2)
        else:
            raise ValueError("Expected F or B")
    assert min_row == max_row
    return min_row


def get_column_id(text: str) -> int:
    min_column = 0
    max_column = 7
    for char in text[7:10]:
        if char == "L":
            max_column = math.floor((min_column + max_column) / 2)
        elif char == "R":
            min_column = math.ceil((min_column + max_column) / 2)
        else:
            raise ValueError("Expected R or L")
    assert min_column == max_column
    return min_column


def decode_ticket(text: str) -> int:
    row_id = get_row_id(text)
    column_id = get_column_id(text)
    return row_id * 8 + column_id
