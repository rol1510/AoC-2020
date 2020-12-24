data = []
with open('input.txt', 'r') as file:
    data = file.readlines()

# returns (direction char, value as int)
def parse_line(line):
    line = line.strip()
    return (
        line[0],
        int(line[1:])
    )

class Ship:
    def __init__(self):
        self.pos_ns = 0
        self.pos_ew = 0
        self.rot = 0

        self.ORDER_MAPPING = {
            'N': self.order_N,
            'S': self.order_S,
            'E': self.order_E,
            'W': self.order_W,
            'R': self.order_R,
            'L': self.order_L,
            'F': self.order_F,
        }

    def follow_order(self, order):
        self.ORDER_MAPPING[order[0]](order[1])

    def order_N(self, arg):
        self.pos_ns -= arg

    def order_S(self, arg):
        self.pos_ns += arg

    def order_E(self, arg):
        self.pos_ew -= arg

    def order_W(self, arg):
        self.pos_ew += arg

    def order_R(self, arg):
        self.rot += arg

    def order_L(self, arg):
        self.rot -= arg

    def order_F(self, arg):
        rot = self.rot % 360
        if rot == 0:     # east
            self.pos_ew -= arg
        elif rot == 90:  # south
            self.pos_ns += arg
        elif rot == 180: # west
            self.pos_ew += arg
        elif rot == 270: # north
            self.pos_ns -= arg
        else:
            raise Exception(f'Ships rotation was not a multiple of 90 (rot:{self.rot})')

    def get_dist_traveled(self):
        return abs(self.pos_ns) + abs(self.pos_ew)

class Ship_with_waypoint:
    def __init__(self, waypoint_start):
        self.waypoint_ns = waypoint_start[0]
        self.waypoint_ew = waypoint_start[1]

        self.pos_ns = 0
        self.pos_ew = 0

        self.ORDER_MAPPING = {
            'N': self.order_N,
            'S': self.order_S,
            'E': self.order_E,
            'W': self.order_W,
            'R': self.order_R,
            'L': self.order_L,
            'F': self.order_F,
        }

    def follow_order(self, order):
        self.ORDER_MAPPING[order[0]](order[1])

    def order_N(self, arg):
        self.waypoint_ns -= arg

    def order_S(self, arg):
        self.waypoint_ns += arg

    def order_E(self, arg):
        self.waypoint_ew -= arg

    def order_W(self, arg):
        self.waypoint_ew += arg

    def order_R(self, arg):
        if arg % 90 != 0:
            raise Exception(f'Rotation value was not a multiple of 90 (rot:{self.rot})')

        rot_clockwise = arg >= 0
        rot = abs(arg) // 90

        for i in range(rot):
            if rot_clockwise:
                tmp = self.waypoint_ew
                self.waypoint_ew = self.waypoint_ns
                self.waypoint_ns = -tmp
            else:
                tmp = self.waypoint_ew
                self.waypoint_ew = -self.waypoint_ns
                self.waypoint_ns = tmp

    def order_L(self, arg):
        self.order_R(-arg)

    def order_F(self, arg):
        self.pos_ns += self.waypoint_ns * arg
        self.pos_ew += self.waypoint_ew * arg

    def get_dist_traveled(self):
        return abs(self.pos_ns) + abs(self.pos_ew)

ship = Ship()
waypoint = Ship_with_waypoint((-1, -10))
for line in data:
    order = parse_line(line)
    ship.follow_order(order)
    waypoint.follow_order(order)

print('Part 1:', ship.get_dist_traveled())
print('Part 2:', waypoint.get_dist_traveled())