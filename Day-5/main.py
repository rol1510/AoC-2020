data = []
with open('input.txt', 'r') as file:
    data = file.read().splitlines()

def binary_search(low, high, binary_string):
    for b in binary_string:
        dif = (high-low)+1

        if b == '1':
            low += dif // 2
        else:
            high -= dif // 2

        if high == low:
            return high

    raise Exception("Binary search die not work as expected")

def decode_input(input_string):
    row = input_string[:7]
    col = input_string[-3:]

    row = row.replace('F', '0').replace('B', '1')
    col = col.replace('L', '0').replace('R', '1')

    return row, col

seat_ids = []
for sample in data:
    row, col = decode_input(sample)

    row_num = binary_search(0, 127, row)
    col_num = binary_search(0, 7, col)#

    seat_id = row_num * 8 + col_num
    seat_ids.append(seat_id)

    print(row, row_num, col, col_num, '=', seat_id)

print('highest seat id:', max(seat_ids))

smallest_id = min(seat_ids)
biggest_id = max(seat_ids)

for i in range(smallest_id, biggest_id):
    if i not in seat_ids:
        print("Empty seat is:", i)