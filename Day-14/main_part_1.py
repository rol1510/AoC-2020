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

def mask_number(number, mask):
    valid_mask = int(mask.replace('1', '0').replace('X', '1'), 2)
    mask_override = int(mask.replace('X', '0'), 2)
    return (number & valid_mask) + mask_override

memory_map = {}
current_mask = None

for line in data:
    if 'mask' in line:
        current_mask = parse_mask(line)
        # print(current_mask)
    else:
        inst = parse_instruction(line)
        memory_map[inst[0]] = mask_number(inst[1], current_mask)

# print(memory_map)
res = sum(memory_map.values())
print('Part 1:', res)