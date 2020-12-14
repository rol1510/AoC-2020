data = []
with open('input.txt', 'r') as file:
    data = file.read().splitlines()

TREE_CHAR  = '#'

def hit_tree(data, x, y):
    return data[y][x%len(data[y])] == TREE_CHAR

def count_trees(data, slope):
    # x -> horizontally, y -> vertically

    trees_hit = 0
    x = 0

    for y in range(0, len(data), slope[0]):
        if hit_tree(data, x, y):
            trees_hit += 1
        x += slope[1]

    return trees_hit

# x -> horizontally, y -> vertically
slopes = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1),
]

res = 1
for slope in slopes:
    hits = count_trees(data, slope)
    res *= hits
    print("Slope:", slope, "trees hit:", hits)
print("Result:", res)
