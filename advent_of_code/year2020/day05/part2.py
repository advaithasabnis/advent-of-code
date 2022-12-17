from collections import defaultdict

from .shared import decode_ticket, get_row_id


def get_rows_with_spaces(tickets):
    seats = defaultdict(int)
    for ticket in tickets:
        seats[ticket[:7]] += 1
    return [k for k, v in seats.items() if v < 8]


# Narrow down search to rows with less than 8 occupied seats
def main(text: str) -> int:
    data = text.splitlines()
    # Rows with less than 8 occupied seats
    empty = get_rows_with_spaces(data)
    # Seat IDs present in these rows
    occupied = [decode_ticket(k) for k in data if k.startswith(tuple(empty))]
    # All allowed seat IDs in these rows
    seat_ids = [get_row_id(r) * 8 + c for r in empty for c in range(0, 8)]
    for seat in seat_ids:
        if (min(occupied) < seat < max(occupied)) and (seat not in occupied):
            return seat
