import re

data = []
with open('input.txt', 'r') as file:
    data = file.read().splitlines()

def is_password_valid(entry):
    info, password = entry.split(':')
    info = info.strip()
    password = password.strip()

    letter = info[-1]
    minimum = int(re.findall('^(\d+)-\d+', info)[0])
    maximum = int(re.findall('^\d+-(\d+)', info)[0])

    occurrences = password.count(letter)

    # part 1
    # return occurrences >= minimum and occurrences <= maximum

    # part 2
    p1 = minimum - 1
    p2 = maximum - 1
    return (password[p1] == letter) ^ (password[p2] == letter)

def count_valid_passwords(data):
    valid = 0
    for entry in data:
        if is_password_valid(entry):
            valid += 1
    return valid
res = count_valid_passwords(data)

print("valid passwords:", res)
