# From https://www.reddit.com/r/adventofcode/comments/1ha27bo/comment/m15ljob/
import heapq
from collections import defaultdict


def main(text: str) -> int:
    lengths = [int(num) for num in text]

    file_positions: dict[int, tuple[int, int]] = {}  # id: (start,length)
    gaps: defaultdict[int, list[int]] = defaultdict(list)  # gap_length: [starts]

    cur_pos = 0
    for i, num in enumerate(lengths):
        if i % 2 == 0:
            file_positions[i // 2] = (cur_pos, num)
        else:
            if num > 0:
                heapq.heappush(gaps[num], cur_pos)
        cur_pos += num

    for i in sorted(file_positions.keys(), reverse=True):
        file_start_pos, file_len = file_positions[i]
        possible_gaps = sorted(
            [[gaps[gap_len][0], gap_len] for gap_len in gaps if gap_len >= file_len]
        )

        if possible_gaps:
            gap_start_pos, gap_len = possible_gaps[0]
            if file_start_pos > gap_start_pos:
                file_positions[i] = (gap_start_pos, file_len)
                remaining_gap_len = gap_len - file_len
                heapq.heappop(gaps[gap_len])
                if not gaps[gap_len]:
                    del gaps[gap_len]
                if remaining_gap_len:
                    heapq.heappush(gaps[remaining_gap_len], gap_start_pos + file_len)

    checksum = sum(
        num * (start * length + (length * (length - 1)) // 2)
        for num, (start, length) in file_positions.items()
    )  # (start) + (start+1) + ... + (start+length-1)

    return checksum


# Original approach which is much slower
# def main(text):
#     data = list(map(int, text))
#     files = data[::2]

#     order = []

#     for idx, size in enumerate(data):
#         if idx % 2 == 0:
#             order.append((idx // 2 + 1, size))
#         else:
#             order.append((0, size))

#     for i in range(len(order))[::-1]:
#         for j in range(i):
#             i_data, i_size = order[i]
#             j_data, j_size = order[j]

#             if i_data and not j_data and i_size <= j_size:
#                 order[i] = (0, i_size)
#                 order[j] = (0, j_size - i_size)
#                 order.insert(j, (i_data, i_size))

#     checksum = 0
#     idx = 0
#     for _, (data, size) in enumerate(order):
#         for _ in range(size):
#             if data:
#                 checksum += idx * (data - 1)
#             idx += 1


assert main('2333133121414131402') == 2858
