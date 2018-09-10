"""
This is a sample test docstring
"""
import unittest
import random as r

from marsrovers import grid as g
from marsrovers import rover as r
from marsrovers import mission as m


class Test(unittest.TestCase):
    """
    Hello test class.
    """

    def setUp(self):
        """ Initialise test suite - no-op. """
        pass

    def tearDown(self):
        """ Clean up test suite - no-op. """
        pass

    def test_case1(self, ):
        """ Test for equal. """
        mars = g.Grid()
        mars.set_size(5, 5)
        rover = r.Rover()
        rover.set_rover(1, 2, "N")
        instructions1 = "LMLMLMLMM"
        mission = m.Mission()
        mission.set_mission(mars, rover, instructions1)
        mission.do_mission()
        res = ' '.join(map(str, mission.rover.get_rover()))
        self.assertEqual(res, "1 3 N")

    def test_case2(self, ):
        """ Test for equal. """
        mars = g.Grid()
        mars.set_size(5, 5)
        rover1 = r.Rover()
        rover1.set_rover(3, 3, "E")
        instructions1 = "MMRMMRMRRM"
        mission1 = m.Mission()
        mission1.set_mission(mars, rover1, instructions1)
        mission1.do_mission()
        res = ' '.join(map(str, mission1.rover.get_rover()))
        self.assertEqual(res, "5 1 E")

    def test_case3(self, ):
        """ Test for equal. """
        mars = g.Grid()
        mars.set_size(5, 5)
        rover1 = r.Rover()
        rover1.set_rover(0, 0, "N")
        instructions1 = "MMMRMMMMMLMRRMMRRMMLMMMLMMMMRMM"
        mission1 = m.Mission()
        mission1.set_mission(mars, rover1, instructions1)
        mission1.do_mission()
        res = ' '.join(map(str, mission1.rover.get_rover()))
        self.assertEqual(res, "0 0 W")


if __name__ == '__main__':
    unittest.main()
