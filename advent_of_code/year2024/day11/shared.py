from functools import lru_cache


def split_string_in_half(s: str) -> tuple[str, str]:
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:].lstrip('0') or '0'
    return left, right


@lru_cache(maxsize=None)
def blink(mark: str, max_blinks: int, blink_num: int = 1) -> int:
    if blink_num > max_blinks:
        return 1
    if mark == '0':
        return blink('1', max_blinks, blink_num + 1)
    elif len(mark) % 2 == 0:
        left, right = split_string_in_half(mark)
        return blink(left, max_blinks, blink_num + 1) + blink(right, max_blinks, blink_num + 1)
    else:
        return blink(str(int(mark) * 2024), max_blinks, blink_num + 1)
