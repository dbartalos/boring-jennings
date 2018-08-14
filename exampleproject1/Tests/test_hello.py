"""
This is a sample test docstring
"""
import unittest

from exampleproject1.hello import hello


class TestHello(unittest.TestCase):
    """
    Hello test class.
    """

    def setUp(self):
        """ Initialise test suite - no-op. """
        pass

    def tearDown(self):
        """ Clean up test suite - no-op. """
        pass

    def test_valid(self):
        """ Test for equal. """
        self.assertEqual("Hello World", hello("Hello World"))

    def test_invalid(self):
        """ Test for not equal. """
        self.assertNotEqual("", hello("test"))


if __name__ == '__main__':
    unittest.main()
