class Bag:
    def __init__(self, color, children):
        self.color = color
        self.parents = []
        self.children = children

    def has_no_children(self):
        return self.children == None or len(self.children) == 0

    def has_no_parents(self):
        return self.parents == None or len(self.parents) == 0

    def add_parent(self, parent):
        if not parent in self.parents:
            self.parents.append(parent)

    def setup_parents_for_children(self):
        for child in self.children:
            child[1].add_parent(self)

    def count_ancestors(self, alread_counted=[]):
        if self.has_no_parents():
            return 0
        else:
            s = 0
            for p in self.parents:
                if not p in alread_counted:
                    s += 1 # for the parent
                    alread_counted.append(p)
                    s += p.count_ancestors(alread_counted) # the ancestors of the parent

            return s

    def count_descendents(self):
        if self.has_no_children():
            return 0
        else:
            count = 0
            for c in self.children:
                count += c[0] # the children itself also count
                count += c[0] * c[1].count_descendents()
            return count

    def __repr__(self):
        return f'Bag in {self.color}'

# returns (this bags color, [(number of other bags, other bag color), ...])
#                           ^ List is None if no bags are contained
# excample: light red bags contain 1 bright white bag, 2 muted yellow bags.
#  returns: ('light red', [(1, 'bright white'), (2, 'muted yellow')])
def parse_bag_data_form_string(as_string):
    def split_contained(contained_bag):
        parts = contained_bag.strip().split(' ')
        return (
            int(parts[0]),
            ' '.join(parts[1:-1])
        )

    parts = as_string.split('bags contain')
    bag_color = parts[0].strip()

    if 'no other bag' in parts[1]:
        other_bags = []
    else:
        other_bags = [split_contained(x) for x in parts[1].split(',')]

    return (bag_color, other_bags)

def get_bag_by_color(color):
    for bag in bags:
        if bag.color == color:
            return bag
    return None

def add_bag(color, children):
    existing = get_bag_by_color(color)

    if existing == None:
        # if not existing now, create a new Bag
        # existing children will be added. If a child does not exist yet,
        # it will still be created, but it's children list will stay empty for now
        new_bag = Bag(
            color,
            [(c[0], add_bag(c[1], [])) for c in children] # will be [(amount, child), ...]
        )
        bags.append(new_bag)
        return new_bag

    else:
        # if the bag exist but has no children yet, we will add the existing children and
        # create 'empty' children for now
        if existing.has_no_children():
            existing.children = [(c[0], add_bag(c[1], [])) for c in children] # will be [(amount, child), ...]
        return existing

data = []
with open('input.txt', 'r') as file:
    data = file.readlines()

bags = []

for line in data:
    bag_data = parse_bag_data_form_string(line)
    add_bag(bag_data[0], bag_data[1])

for bag in bags:
    bag.setup_parents_for_children()

print('unique bags:', len(bags))

TRAGET_BAG_COLOR = 'shiny gold'

target_bag = next(b for b in bags if b.color == TRAGET_BAG_COLOR)
print('target:', target_bag)
print(f'ancestors for {target_bag}:  ', target_bag.count_ancestors())
print(f'descendents for {target_bag}:', target_bag.count_descendents())