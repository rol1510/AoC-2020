data = []
with open('input.txt', 'r') as file:
    data = file.readlines()

earliest_time = int(data[0].strip())
bus_ids = [int(x.strip()) for x in data[1].split(',') if x != 'x']

# print(earliest_time)
# print(bus_ids)

smallest_wait_time = 9999999
smallest_wait_id = -1
for bus_id in bus_ids:
    wait_time = bus_id - (earliest_time % bus_id)
    if wait_time < smallest_wait_time:
        smallest_wait_id = bus_id
        smallest_wait_time = wait_time

print('Part 1:', smallest_wait_time * smallest_wait_id)