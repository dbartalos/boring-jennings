from collections import deque as dq
from marsrovers.enumerators import Directions as d


class Rover():
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.directions = dq([['W', (-1, 0)], ['N', (0, 1)],
                              ['E', (1, 0)], ['S', (0, -1)]])

    def get_rover(self):
        return (self.x, self.y, self.direction)

    def set_rover(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction
        self.set_direction(direction)

    def get_coordinates(self):
        return [self.x, self.y]

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_direction(self):
        return (self.direction)

    def set_direction(self, direction):
        while (self.check_direction(self.direction)) \
                and (self.directions[0][0] != direction):
            self.turn_left()

    def check_direction(self, direction):
        try:
            assert hasattr(d, direction)
        except:
            raise Exception("Invalid direction:%s" % (direction))
        return True

    def turn_left(self):
        self.directions.appendleft(self.directions.pop())
        self.direction = self.directions[0][0]

    def turn_right(self):
        self.directions.append(self.directions.popleft())
        self.direction = self.directions[0][0]

    def __repr__(self):
        return ' '.join(map(str, self.get_rover()))


r1 = Rover()
r1.set_rover(10, 9, "N")
print(r1)
