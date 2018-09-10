"""
This is a sample test docstring
"""
import unittest
import random as r

from marsrovers import rover


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

    def test_size(self, ):
        """ Test for equal. """
        x, y = r.randint(2, 100), r.randint(2, 100)
        rov = rover.Rover()
        rov.set_rover(x, y, "N")
        self.assertEqual(rov.get_direction(), "N")


if __name__ == '__main__':
    unittest.main()
