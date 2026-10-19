import unittest 
from temperatuur import fahrenheit2celsius
from temperatuur import celsius2fahrenheit
from temperatuur import celsius2kelvin
from temperatuur import fahrenheit2kelvin

class TestTemperatuurConversies(unittest.TestCase):

    def test_fahrenheit2celsius(self): 
        self.assertAlmostEqual(fahrenheit2celsius(32), 0) 
        self.assertAlmostEqual(fahrenheit2celsius(212), 100) 
        self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
        self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)

    def test_celsius2fahrenheit(self): 
        self.assertAlmostEqual(celsius2fahrenheit(0), 32) 
        self.assertAlmostEqual(celsius2fahrenheit(100), 212) 
        self.assertAlmostEqual(celsius2fahrenheit(35), 95)

    def test_celsius2kelvin(self): 
        self.assertAlmostEqual(celsius2kelvin(0), 273.15) 
        self.assertAlmostEqual(celsius2kelvin(100), 373.15) 
        self.assertAlmostEqual(celsius2kelvin(35), 308.15)

    def test_fahrenheit2kelvin(self): 
        self.assertAlmostEqual(fahrenheit2kelvin(32), 273.15) 
        self.assertAlmostEqual(fahrenheit2kelvin(212), 373.15) 
        self.assertAlmostEqual( fahrenheit2kelvin(35), 274.8166667 )

if __name__ == "main": unittest.main()

# Uitvoeren in de terminal met commando:
# $ python -m unittest -v test_temperatuur.py