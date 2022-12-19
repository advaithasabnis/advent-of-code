def find_marker(text: str, window_size: int) -> int:
    for i in range(len(text) - window_size + 1):
        if len(set(text[i : i + window_size])) == window_size:
            return i + window_size
    else:
        raise ValueError("No solution found")
