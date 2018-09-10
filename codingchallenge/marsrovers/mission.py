import marsrovers.grid as g
import marsrovers.rover as r
from marsrovers.enumerators import Instructions as inst


class Mission():
    def __init__(self):
        self.grid = None
        self.rover = None
        self.instructions = None

    def get_mission(self):
        return (self.grid, self.rover, self.instructions)

    def set_mission(self, g, r, i):
        self.grid = g
        self.rover = r
        self.instructions = i
        self.check_mission_instructions()
        self.check_mission(self.rover.x, self.rover.y)

    def get_mission_state(self):
        return (self.rover.get_position())

    def print_mission_state(self):
        print(' '.join(map(str, self.rover.get_position())))

    def check_mission_instructions(self):
        for instruction in list(self.instructions):
            try:
                assert hasattr(inst, instruction)
            except:
                raise Exception("Invalid instuction: %s" % (instruction))

    def check_mission(self, x, y):
        try:
            assert ((x >= 0) and (x <= self.grid.width) and
                    (y >= 0) and (y <= self.grid.height))
        except:
            raise Exception("Invalid coordinates x:%d y%d"
                            % (x, y))

        return True

    def move_rover(self):
        x1 = self.rover.get_coordinates()[0]
        y1 = self.rover.get_coordinates()[1]
        x2 = self.rover.directions[0][1][0]
        y2 = self.rover.directions[0][1][1]
        self.check_mission(x1 + x2, y1 + y2)
        self.rover.set_coordinates(x1 + x2, y1 + y2)

    def do_mission(self):
        for instruction in list(self.instructions):
            if(instruction == inst["Left"].value):
                self.rover.turn_left()
            if(instruction == inst["Right"].value):
                self.rover.turn_right()
            if(instruction == inst["Move"].value):
                self.move_rover()


mars = g.Grid()
mars.set_size(5, 5)
rover1 = r.Rover()
rover1.set_rover(1, 2, "N")
instructions1 = "LMLMLMLMM"
mission1 = Mission()
mission1.set_mission(mars, rover1, instructions1)
mission1.do_mission()

rover2 = r.Rover()
rover2.set_rover(3, 3, "E")
instructions2 = "MMRMMRMRRM"
mission2 = Mission()
mission2.set_mission(mars, rover2, instructions2)
mission2.do_mission()
