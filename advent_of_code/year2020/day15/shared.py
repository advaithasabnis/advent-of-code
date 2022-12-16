def find_last_spoken(starting_numbers, stop_turn):
    record = [0] * stop_turn
    for i, j in enumerate(starting_numbers):
        record[j] = i + 1
    next_spoken = 0
    for t in range(len(starting_numbers) + 1, stop_turn):
        spoken = next_spoken
        if record[spoken] > 0:
            next_spoken = t - record[spoken]
        else:
            next_spoken = 0
        record[spoken] = t
    return next_spoken
