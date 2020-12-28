import re

data = []
with open('input.txt', 'r') as file:
    data = file.readlines()

# input: 'mem[mem_index] = value'
# returns (mem_index, value)
def parse_instruction(line):
    res = re.findall('\\d+', line)
    return (int(res[0]), int(res[1]))

def parse_mask(line):
    return line.split(' ')[-1].strip()

def to_bin_str(number, pad_to):
    res = bin(number).split('b')[1].strip()
    padding = '0' * (pad_to - len(res))
    return padding + res

def mask_number(number, mask):
    number = to_bin_str(number, len(mask))

    res = ''
    for m, n in zip(mask, number):
        if m == 'X' or m == '1':
            res += m
        elif m == '0':
            res += n
        else:
            Exception('Mask is invalid')

    return res

def replace_floating(string, replacement):
    assert string.count('X') == len(replacement)
    indices = [index for index, x in enumerate(string) if x == 'X']

    res = list(string)
    for j, i in enumerate(indices):
        res[i] = replacement[j]
    return ''.join(res)

def possible_addresses(address):
    counts = address.count('X')
    possible = 2**counts
    for i in range(possible):
        i_str = to_bin_str(i, counts)
        res = replace_floating(address, i_str)
        yield int(res, 2)


memory_map = {}
current_mask = None

for line in data:
    if 'mask' in line:
        current_mask = parse_mask(line)
        # print(current_mask)
    else:
        inst = parse_instruction(line)
        # print(inst)
        address = mask_number(inst[0], current_mask)
        for real_addr in possible_addresses(address):
            # print(real_addr)
            memory_map[real_addr] = inst[1]

# print(memory_map)
res = sum(memory_map.values())
print('Part 2:', res)