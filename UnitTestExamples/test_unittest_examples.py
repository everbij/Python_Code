import unittest

from unittest_examples import fahrenheit2celsius

class TestTemperatuurConversies(unittest.TestCase):

    def test_fahrenheit2celsius(self): 
        print("Test met AlmostEqual")
        self.assertAlmostEqual(fahrenheit2celsius(32), 0)
        self.assertAlmostEqual(fahrenheit2celsius(212), 100) 
        self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
        self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)
    
    def test_fahrenheit2celsius(self): 
        print("Test met Equal")
        self.assertEqual(fahrenheit2celsius(32), 0)
        self.assertEqual(fahrenheit2celsius(212), 100) 
        self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
        self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)
    
    if __name__ == "main": unittest.main()
