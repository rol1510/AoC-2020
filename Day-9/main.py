import itertools

data = []
with open('input.txt', 'r') as file:
    data = [int(x) for x in file.readlines()]

def is_valid(number, number_set):
    for a, b in itertools.combinations(number_set, 2):
        if a+b == number:
            return True
    return False

def find_subset_of_size(target, number_set):
    for i in range(0, len(number_set)):
        for j in range(i+1, len(number_set)):
            subset = number_set[i:j]
            if sum(subset) == target:
                return subset

PREAMBLE_LEN = 25

for i in range(PREAMBLE_LEN, len(data)):
    if is_valid(data[i], data[i-PREAMBLE_LEN:i]) == False:
        invalid_number = data[i]
        print('Part 1 Not valid for:', invalid_number)

        sum_range = find_subset_of_size(invalid_number, data)
        res = min(sum_range) + max(sum_range)
        print('Part 2 result:', res)
        break
