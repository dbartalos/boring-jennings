import os
import fileinput
import marsrovers.grid as g
import marsrovers.rover as r
import marsrovers.mission as m


def main():
    mission = []
    home_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(os.sep, home_dir, "Tests", "input")
    for line in fileinput.input(test_dir):
        if(fileinput.filelineno() == 1):
            width, height = line.strip().split(' ')
            mission.append([width, height])
        elif(fileinput.filelineno() % 2 == 0):
            x, y, direction = line.strip().split(' ')
            mission.append([x, y, direction])
        elif(fileinput.filelineno() % 2 == 1):
            instructions = line.strip()
            mission.append(instructions)

    mars = g.Grid()
    mars.set_size(*mission[0])
    for rx, inst in zip(mission[1::2], mission[2::2]):
        mission = m.Mission()
        rover = r.Rover()
        rover.set_rover(*rx)
        mission.set_mission(mars, rover, inst)
        mission.do_mission()
        mission.print_mission_state()

if __name__ == "__main__":
    main()
