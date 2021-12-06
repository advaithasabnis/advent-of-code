from collections import Counter


def fish_population(starting_fish, age):
    fish_ages = Counter(starting_fish)
    for i in range(age):
        fish_ages = {n - 1: fish_ages[n] for n in range(0, 9)}
        fish_ages[8] = fish_ages[-1]
        fish_ages[6] += fish_ages[-1]
        fish_ages[-1] = 0
    return sum(fish_ages.values())
