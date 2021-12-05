def measure(text, window_size):
    data = list(map(int, text.split()))
    count = 0
    for i in range(window_size, len(data)):
        if data[i] > data[i - window_size]:
            count += 1
    return count
