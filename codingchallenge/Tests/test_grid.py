"""
This is a sample test docstring
"""
import unittest
import random as r

from marsrovers import grid


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
        g = grid.Grid()
        g.set_size(x, y)
        self.assertEqual(g.get_size(), [x, y])

    # def test_invalid(self):
    #     """ Test for not equal. """
    #     self.assertNotEqual("", hello("test"))


if __name__ == '__main__':
    unittest.main()
