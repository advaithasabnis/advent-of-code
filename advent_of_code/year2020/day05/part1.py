from .shared import decode_ticket


# Maximizing row*8 + column same as maximizing row then column
# since column is in range(0,8)
def get_max_row(tickets):
    f = tickets
    s = []
    for i in range(7):
        for ticket in f:
            if ticket[i] == 'B':
                s.append(ticket)
        if len(s) > 0:
            f = s
            s = []
    return f


def get_max_column(tickets):
    f = tickets
    s = []
    for i in range(7, 10):
        for ticket in f:
            if ticket[i] == 'R':
                s.append(ticket)
        if len(s) > 0:
            f = s
            s = []
    assert len(f) == 1
    return f[0]


# First find the max ticket string then only decode it
def main(text: str) -> int:
    data = text.splitlines()
    max_ticket = get_max_column(get_max_row(data))
    return decode_ticket(max_ticket)


# # Decode all ticket strings and get the max seat id (slower)
# def main(text: str) -> int:
#     return max(decode_ticket(ticket) for ticket in text.splitlines())
