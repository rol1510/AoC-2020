STARTING_NUMBERS = [
    [0,3,6], # Part 1: 436   Part 2: 175594
    [1,3,2], # Part 1: 1     Part 2: 2578
    [2,1,3], # Part 1: 10    Part 2: 3544142
    [1,2,3], # Part 1: 27    Part 2: 261214
    [2,3,1], # Part 1: 78    Part 2: 6895259
    [3,2,1], # Part 1: 438   Part 2: 18
    [3,1,2], # Part 1: 1836  Part 2: 362

    [9,6,0,10,18,2,1],
]

TARGET_1 = 2020
TARGET_2 = 30_000_000

def find_last_spoken(starting_numbers, target=2020):
    spoken_index = {}
    for i, n in enumerate(starting_numbers[:-1]):
        spoken_index[n] = i + 1

    last_spoken = starting_numbers[-1]
    for i in range(len(starting_numbers), target):
        if last_spoken in spoken_index.keys():
            tmp = last_spoken
            last_spoken = i - spoken_index[last_spoken]
            spoken_index[tmp] = i
        else:
            spoken_index[last_spoken] = i
            last_spoken = 0
    return last_spoken

print('Part 1:')
for numbers in STARTING_NUMBERS:
    print(f'{numbers} -> {TARGET_1}th spoken {find_last_spoken(numbers, TARGET_1)}')

print('Part 2:')
for numbers in STARTING_NUMBERS:
    print(f'{numbers} -> {TARGET_2}th spoken {find_last_spoken(numbers, TARGET_2)}')
