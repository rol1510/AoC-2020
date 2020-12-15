
REQUIRED_KEYS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    #'cid',
]

data = []
with open('input.txt', 'r') as file:
    data = file.read().split('\n\n')

def parse_passport(data):
    data = data.replace(' ', '\n')
    pairs = data.splitlines()
    # print(pairs)

    res = {}
    for pair in pairs:
        key, value = pair.split(':')
        res[key] = value

    return res

def contains_all(target, required):
    for req in required:
        if req not in target:
            return False
    return True

def between(low, high, x):
    return x >= low and x <= high

def convert_value_to_int(value):
    try:
        return int(value)
    except:
        print("!!!! convert_passport_value_to_int failed !!!! value:", value)
        return None

def convert_passport_value_to_int(key, passport):
    res = convert_value_to_int(passport[key])
    if res != None:
        passport[key] = res
        return True
    else:
        print("!!!! convert_passport_value_to_int failed !!!!", key, ":", passport[key])
        return False

def validate_value_between(passport, key, low, high, digits=-1):
    # Check number of digits if needed
    if digits >= 0:
        if len(str(passport[key])) != digits:
            return False

    # Check if the value is a number
    if not convert_passport_value_to_int(key, passport):
        return False

    return between(low, high, passport[key])

def validate_height(passport, key, minMaxCm, minMaxIn):
    value = passport[key]
    isMetric = False
    minMax = None

    if 'cm' in value:
        isMetric = True
        minMax = minMaxCm
        value = value.replace('cm', '')
    elif 'in' in value:
        isMetric = False
        minMax = minMaxIn
        value = value.replace('in', '')
    else:
        # on unit, value not valid
        return False

    # Check if the value is a number
    res = convert_value_to_int(value)
    if res == None:
        return False
    else:
        return between(minMax[0], minMax[1], res)

def validate_hair_color(passport, key):
    value = passport[key].strip()

    if len(value) != 7 or value[0] != '#':
        return False

    color = value[1:]
    for c in color:
        if not between('0', '9', c) and not between('a', 'f', c):
            return False
    return True

def validate_passport_id(passport, key):
    value = passport[key].strip()
    if len(value) != 9:
        return False

    for c in value:
        if not between('0', '9', c):
            return False
    return True



def is_passport_valid(passport):
    if not contains_all(passport.keys(), REQUIRED_KEYS):
        return False

    # Part 1
    # return True

    # Part 2
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return validate_value_between(passport, 'byr', 1920, 2002, 4) and \
           validate_value_between(passport, 'iyr', 2010, 2020, 4) and \
           validate_value_between(passport, 'eyr', 2020, 2030, 4) and \
           validate_height(passport, 'hgt', (150, 193), (59, 76)) and \
           validate_hair_color(passport, 'hcl')                   and \
           passport['ecl'] in valid_eye_colors                    and \
           validate_passport_id(passport, 'pid')

valid = 0
for passport_raw in data:
    passport_parsed = parse_passport(passport_raw)
    # Part 1
    # if contains_all(passport_parsed.keys(), REQUIRED_KEYS):
    #     valid += 1

    # Part 2
    if is_passport_valid(passport_parsed):
        valid += 1

print('valid:', valid)

# _ = parse_passport(data[0])
# _['byr'] = '2000'
# _['iyr'] = '1000'
# _['hgt'] = '1000'
# print(validate_value_between(_, 'byr', 1920, 2002))
# print(validate_value_between(_, 'iyr', 1920, 2002))