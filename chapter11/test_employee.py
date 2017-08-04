import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test case for employee class."""

    def setUp(self):
        """Default setup for the rest of unittests."""
        self.smith = Employee('john','smith',10000)

    def test_default_raise(self):
        """Test the default raise."""
        self.smith.give_raise()
        self.assertEqual(self.smith.salary, 15000)

    def test_custom_raise(self):
        """Test that the custom raise works."""
        self.smith.give_raise(2000)
        self.assertEqual(self.smith.salary, 12000)

unittest.main()