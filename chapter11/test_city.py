import unittest
from city import city_country

class TestNames(unittest.TestCase):
    """Test city.py"""

    def test_names(self):
        """Test whether the function works for city, country input."""
        name = city_country('santiago','chile')
        self.assertEqual(name, 'Santiago, Chile')

    def test_population(self):
        """Test whether the function works if provided population."""
        full = city_country('santiago','chile',500)
        self.assertEqual(full,'Santiago, Chile - Population 500')


unittest.main()