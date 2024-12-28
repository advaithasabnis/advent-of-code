from collections import defaultdict


def find_next_number(x: int) -> int:
    x = x ^ (x << 6) & 0xFFFFFF
    x = x ^ (x >> 5)  # Mask isn't needed
    x = x ^ (x << 11) & 0xFFFFFF
    return x


def main(text: str) -> int:
    # differences => total price dictionary
    price: dict[int, int] = defaultdict(int)

    for line in text.splitlines():
        # Set of differences seen so far for a monkey
        seen: set[int] = set()
        diffs: int = 0
        x = int(line)
        prev_mod = x % 10

        # Handle the first 4 iterations separately to avoid length checks
        for _ in range(4):
            x = find_next_number(x)
            new_mod = x % 10
            d = (new_mod - prev_mod) & 0x1F
            prev_mod = new_mod
            diffs = (diffs << 5) | d

        for _ in range(1996):
            x = find_next_number(x)
            new_mod = x % 10
            d = (new_mod - prev_mod) & 0x1F
            prev_mod = new_mod
            diffs = ((diffs << 5) & ((1 << 20) - 1)) | d
            # If the differences haven't been seen before, add the price to the dictionary
            if diffs not in seen:
                seen.add(diffs)
                price[diffs] += new_mod

    return max(price.values())
