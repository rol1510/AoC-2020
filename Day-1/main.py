
data = []
with open('input.txt', 'r') as file:
    data = [int(x) for x in file.readlines()]

# print(data)

def find_matching_two(data):
    i = 0
    while i < len(data):
        j = i + 1
        while j < len(data):
            if data[i] + data[j] == 2020:
                return data[i], data[j]
            j += 1
        i += 1

def find_matching_three(data):
    i = 0
    while i < len(data):
        j = i + 1
        while j < len(data):
            k = j + 1
            while k < len(data):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i], data[j], data[k]
                k += 1
            j += 1
        i += 1



res = find_matching_two(data)
print('  Two entries:', res[0], '*', res[1], '=',  res[0]*res[1])

res = find_matching_three(data)
print('Three entries:', res[0], '*', res[1], '*', res[2], '=',  res[0]*res[1]*res[2])