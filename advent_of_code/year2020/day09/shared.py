def find_invalid_num(data, p):
    for n in range(p, len(data)):
        prev = set(data[n - p : n])
        for i in prev:
            if (j := data[n] - i) in prev and j != i:
                break
        else:
            return n, data[n]
