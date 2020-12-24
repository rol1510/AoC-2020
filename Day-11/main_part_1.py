import copy

EMPTY = 'L'
USED  = '#'
FLOOR = '.'

data = []
with open('input.txt', 'r') as file:
    data = [list(x.strip()) for x in file.readlines()]


def pad_data(data, char):
    # pad sides
    for i in range(len(data)):
        data[i].insert(0, char)
        data[i].append(char)

    # pad top and bottom
    width = len(data[0])
    top_bottom_padding = list(char*width)
    data.insert(0, top_bottom_padding)
    data.append(top_bottom_padding)

def format_data(data):
    res = ''
    for line in data:
        res += ''.join(line)
        res += '\n'
    return res

def count_occupied_neighbours(x, y, data):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if data[i][j] == USED:
                count += 1
    return count

def simulate(data):
    new_data = copy.deepcopy(data)
    for x in range(1, len(data)-1):
        for y in range(1, len(data[0])-1):
            neighbours = count_occupied_neighbours(x, y, data)
            current = data[x][y]
            if current == EMPTY and neighbours == 0:
                new_data[x][y] = USED
            elif current == USED and neighbours >= 4:
                new_data[x][y] = EMPTY

    return new_data

def compare_data(data_1, data_2):
    set1 = set(map(tuple, data_1))
    set2 = set(map(tuple, data_2))
    diff = set1.symmetric_difference(set2)
    return len(diff) == 0

def count_occupied_seats(data):
    count = 0
    for line in data:
        count += line.count(USED)
    return count

pad_data(data, FLOOR)

new_data = data
data = []
interations = 0
while compare_data(data, new_data) == False:
    data = new_data
    new_data = simulate(data)
    interations += 1
    # print(format_data(data))


print('iterations:', interations)
print('Part 1:', count_occupied_seats(new_data))