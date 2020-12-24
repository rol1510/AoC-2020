from collections import deque
import time

data = []
with open('input.txt', 'r') as file:
    data = [int(x) for x in file.readlines()]

start = time.time()

#add the source
data.append(0)
#add the build in adapter of the device
data.append(max(data)+3)
data.sort()

def rotate_list(data, amount):
    d = deque(data)
    d.rotate(amount)
    return list(d)

differences_count = {}
for a, b in zip(data, rotate_list(data, -1)):
    dif = b-a

    if dif < 0:
        # will be the diff between in build and soure, so we are done here
        break

    if dif in differences_count.keys():
        differences_count[dif] += 1
    else:
        differences_count[dif] = 1

print("differences_counted:", differences_count)
print('Part 1:', differences_count[1] * differences_count[3])

# Explanation Part 2
#
# from part 1 we know there won't be any chargers with a delta of 2.
# If the delta is 3, nothing can change here, but if there is a coherent series of 1's,
# we can figure out that for a size n, there are x(n) possibilities
# to get all the possibilities we can simplie multiplay the possibilites of those single series
#
# n=2 x=2  (11    -> 11, 2)
# n=3 x=4  (111   -> 111, 12, 21, 3)
# n=4 x=7  (1111  -> 1111, 211, 121, 112, 22, 31, 13)
# n=5 x=13 (11111 -> 11111, 2111, 1211, 1121, 1112, 221, 212, 122, 311, 131, 113, 32, 23)
# ....
#
# now if we look up 1,2,4,7,13 at oeis.org we find out its the Tribonacci number sequence
#
# for example:
#          series of 3  series of 2
#           ---------    --------
# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10,     12, 15, 16, 19, (22)
# (0), 1, 4, 5,    7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5,    7, 10,     12, 15, 16, 19, (22)
# (0), 1, 4,    6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4,    6, 7, 10,     12, 15, 16, 19, (22)
# (0), 1, 4,       7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4,       7, 10,     12, 15, 16, 19, (22)
#
# possibilities = x(3) * x(2) = 4 * 2 = 8

def get_deltas(series):
    deltas = []
    for a, b in zip(series, rotate_list(series, -1)):
        # print(a,b)
        dif = b-a

        if dif < 0:
            # will be the diff between in build and soure, so we are done here
            return deltas

        deltas.append(dif)

    raise Exception('Something bad happend')

deltas = get_deltas(data)


# could not find a simple formula, so in this case a lookup table works well enough
POSSIBILITIES_LOOKUP_TABLE = {
    1:  1,
    2:  2,
    3:  4,
    4:  7,
    5:  13,
    6:  24,
    7:  44,
    8:  81,
    9:  149,
    10: 274,
    11: 504,
    12: 927,
    13: 1705,
    14: 3136,
    15: 5768,
    16: 10609,
    17: 19513,
    18: 35890,
    19: 66012,
    20: 121415,
    21: 223317,
    22: 410744,
    23: 755476,
    24: 1389537,
    25: 2555757,
    26: 4700770,
    27: 8646064,
    28: 15902591,
    29: 29249425,
    30: 53798080,
    31: 98950096,
    32: 181997601,
    33: 334745777,
    34: 615693474,
    35: 1132436852,
}

def get_all_repeating_lengths(data, target):
    res = []
    count = 0

    for x in data:
        if x == target:
            count += 1
        else:
            if count != 0:
                res.append(count)
                count = 0

    return res

segments_of_ones = get_all_repeating_lengths(deltas, 1)

# change 3 to 8 (explained above)
segments_of_ones = [POSSIBILITIES_LOOKUP_TABLE[s] for s in segments_of_ones]

# get the product of the resulting elements
res = 1
for s in segments_of_ones:
    res *= s

# print(segments_of_ones)
print('Part 2 possible combinations:', res)
print('Time to calculate possibilities spend:', (time.time() - start) * 1000, 'ms')
