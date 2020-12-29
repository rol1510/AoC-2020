import re

SEPERATOR_MY_TICKET = 'your ticket:'
SEPERATOR_NEARBY_TICKETS = 'nearby tickets:'

data = []
with open('input.txt', 'r') as file:
    data = file.read()

def split_data(data):
    info, other = data.split(SEPERATOR_MY_TICKET)
    my_ticket, nearby_tickets = other.split(SEPERATOR_NEARBY_TICKETS)

    return ( info.strip().splitlines(),
             my_ticket.strip(),
             nearby_tickets.strip().splitlines() )

def parse_range(data):
    low, high = data.strip().split('-')
    return (int(low), int(high))

# returns ('identifier', [(low, high), ...])
def parse_info_data_line(info_data):
    identifier, data = info_data.split(':')
    ranges_data = data.split('or')

    ranges = []
    for entry in ranges_data:
        ranges.append(parse_range(entry))

    return (identifier.strip(), ranges)

def parse_info_data(info_data):
    res = []
    for line in info_data:
        res.append(parse_info_data_line(line))
    return res

def parse_ticket_data(data):
    parts = data.strip().split(',')
    return [int(x) for x in parts]

def parse_nearby_tickets_data(data):
    res = []
    for line in data:
        res.append(parse_ticket_data(line))
    return res

def layout_ranges(ranges):
    res = []
    for r in ranges:
        for x in range(r[0], r[1]+1):
            if not x in res:
                res.append(x)
    return res

def layout_ranges_of_infos(infos):
    res = []
    for info in infos:
        res.append(
            (info[0], layout_ranges(info[1]))
        )
    return res

def collect_ranges_from_info(infos):
    res = []
    for i in infos:
        for x in i[1]:
            res.append(x)
    return res

def is_ticket_valid(ticket, valid_numbers):
    invalid = []
    for n in ticket:
        if not n in valid_numbers:
            invalid.append(n)
    return len(invalid) < 1, invalid

def filter_valid_tickets(tickets, valid_numbers):
    error_rate = 0
    valid = []

    for ticket in tickets:
        is_valid, errors = is_ticket_valid(ticket, valid_numbers)
        error_rate += sum(errors)
        if is_valid:
            valid.append(ticket)

    return valid, error_rate

# think of it as transforming a list like [row, row, row] to a list [column, column, column]
def group_fields_together(tickets):
    res = []
    for x in zip(*tickets):
        res.append(list(x))
    return res

# add some data and a placeholder to the clue
# returns [[[], clue, index], ...]
def prep_clue_list(clues):
    res = []
    for i, c in enumerate(clues):
        res.append([[], c, i])
    return res

def info_fits_clue(info, clue):
    for number in clue[1]:
        if not number in info[1]:
            return False
    return True

def fit_info_to_clues(info, clues):
    for clue in clues:
        if info_fits_clue(info, clue):
            clue[0].append(info[0])

def count_occurrences(clues):
    # {key: [occurrences]}
    res = {}
    for clue in clues:
        for x in clue[0]:
            if x in res.keys():
                res[x].append(clue[2])
            else:
                res[x] = [clue[2]]
    return res

def remove_clue(clues, index, key):
    for clue in clues:
        if key in clue[0]:
            clue[0].remove(key)

        if clue[2] == index:
            clues.remove(clue)

def remove_certain_results(clues):
    certain_clues = count_occurrences(clues)
    res = []

    for key, occurrences in certain_clues.items():
        if len(occurrences) == 1:
            index = occurrences[0]
            remove_clue(clues, index, key)
            res.append((key, index))
    return res

def solve_order(clues, infos_layed_out):
    for info in infos_layed_out:
        fit_info_to_clues(info, clues)

    res = []
    while True:
        removed = remove_certain_results(clues)
        if removed == [] or len(removed) == 0:
            break
        else:
            for e in removed:
                res.append(e)
    return res

def map_order_to_ticket(order, ticket):
    assert len(order) == len(ticket)
    sorted_order = sorted(order, key=lambda x: x[1])
    res = []
    for name, index in sorted_order:
        res.append((name, ticket[index]))
    return res

def get_part_2_result(mapped_order):
    res = 1
    for e in mapped_order:
        if 'departure' in e[0]:
            res *= e[1]
    return res

info_data, my_ticket_data, nearby_tickets_data = split_data(data)

infos = parse_info_data(info_data)
my_ticket = parse_ticket_data(my_ticket_data)
nearby_tickets = parse_nearby_tickets_data(nearby_tickets_data)

# highest value ist < 1000, so will be fine for this case
all_ranges = collect_ranges_from_info(infos)
ranges_layed_out = layout_ranges(all_ranges)

valid_tickets, error_rate = filter_valid_tickets(nearby_tickets, ranges_layed_out)

print('Part 1:', error_rate)

# print(infos)
# print(my_ticket)
# print(valid_tickets)

fields = group_fields_together(valid_tickets)
infos_layed_out = layout_ranges_of_infos(infos)

# should have made a class for a clue, would have been waaay nicer
clues = prep_clue_list(fields)

order = solve_order(clues, infos_layed_out)
mapped_order = map_order_to_ticket(order, my_ticket)
result_part_2 = get_part_2_result(mapped_order)

# print(mapped_order)
print('Part 2:', result_part_2)

