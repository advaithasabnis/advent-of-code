def is_valid(data: list[int], allow_removal: bool = False) -> bool:
    for i in range(len(data) - 1):
        # Check if the difference between two elements is between 1 and 3
        if not 1 <= data[i] - data[i + 1] <= 3:
            if not allow_removal:
                return False
            # Try removing the element at index i or i + 1 to check validity
            return is_valid(data[:i] + data[i + 1 :]) or is_valid(data[: i + 1] + data[i + 2 :])

    return True
