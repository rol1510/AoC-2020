data = []
with open('input.txt', 'r') as file:
    data = file.readlines()

# returns (instruction string, argument as an int)
def parse_line(line):
    inst, arg = line.split(' ')[0:2]
    return (
        inst.strip(),
        int(arg)
    )

def inst_acc(arg):
    global accumulator
    accumulator += arg

def inst_jmp(arg):
    global prog_counter
    # -1 because prog_counter get incremented for every instruction
    prog_counter += arg - 1

def inst_nop(arg):
    pass

def run_inst(inst):
    if inst[0] in MAPPING_TABLE:
        MAPPING_TABLE[inst[0]](inst[1])

accumulator = 0
prog_counter = 0

MAPPING_TABLE = {
    'acc': inst_acc,
    'jmp': inst_jmp,
    'nop': inst_nop,
}

# returns (Loop detected, last prog_counter, last accumulator)
def simulate(instructions):
    global accumulator, prog_counter
    # reset
    accumulator = 0
    prog_counter = 0

    lines_hit = []
    while prog_counter < len(data):
        if prog_counter in lines_hit:
            return (True, prog_counter, accumulator)
        else:
            lines_hit.append(prog_counter)

        inst = instructions[prog_counter]
        run_inst(inst)
        prog_counter += 1

    return (False, prog_counter, accumulator)

instructions = []
for line in data:
    instructions.append(parse_line(line))

res = simulate(instructions)
print(f'Part 1: Accumulator is {res[2]}')

index = 0
while index < len(instructions):
    current_inst = instructions[index]
    if current_inst[0] != 'acc':
        instructions_copy = instructions.copy()
        instructions_copy[index] = ('jmp' if instructions_copy[index][0] == 'nop' else 'nop',
                                    instructions_copy[index][1])
        # print(instructions_copy)
        res = simulate(instructions_copy)
        if res[0] == False:
            print(f'Part 2: Accumulator is {res[2]}')

    index += 1