import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for name_function.py"""

    def test_first_last_name(self):
        """Do names like David Malan work."""
        formatted_name = get_formatted_name('david', 'Malan')
        self.assertEqual(formatted_name, 'David Malan')

    def test_three(self):
        """Do middle names work."""
        name = get_formatted_name('david', 'malan', 'j')
        self.assertEqual(name, 'David J Malan')

unittest.main()