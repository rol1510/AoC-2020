import time
from math import gcd, lcm

data = []
with open('input.txt', 'r') as file:
    data = file.readlines()

# data = ['', '1789,37,47,1889']

# [(index, bus_id), ...]
bus_ids = [(int(x.strip()), i) for i, x in enumerate(data[1].split(',')) if x != 'x']
print(bus_ids)

# return (new_start, multiple)
def calc(start, multiple_1, multiple_2, offset_2):
    res = []
    t = start
    while True:
        if (t + offset_2) % multiple_2 == 0:
            res.append(t)
            if len(res) >= 2:
                return (res[0], res[1]-res[0])
        t += multiple_1

res = (0, bus_ids[0][0])
for bus_id in bus_ids:
    res = calc(res[0], res[1], bus_id[0], bus_id[1])

print('Part 2:', res[0])
