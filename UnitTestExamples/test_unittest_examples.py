import unittest

from unittest_examples import fahrenheit2celsius
from unittest_examples import add
from unittest_examples import divide
from unittest_examples import priemgetalbepalen
from unittest_examples import return_values
from datetime import date

class TestTemperatuurConversies(unittest.TestCase):

# #   testen van assertAlmostEqual
#     def test_fahrenheit2celsius(self): 
#         print("Test met AlmostEqual")
#         self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
#         self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)
    
#     def test_fahrenheit2celsius(self): 
#         print("Test met Equal")
#         self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
#         self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)

# #   testen van assertEqual
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -2), -3)

#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, -2), -1)
#         self.assertEqual(add(-1, 2), 1)

# #   testen van assertAlmostEqual
#     def test_devide_positive_numbers(self):
#         self.assertAlmostEqual(divide(2, 3),0.66667, 5)

# #   testen van assertTrue en assertFalse
#     def test_priemgetal(self): 
#         self.assertTrue(priemgetalbepalen(7)) 
#         self.assertTrue(priemgetalbepalen(17))


#   testen van assertGreater en assertLess
    def greater_or_smaller(self):
    #    print("greater or smaller")
        self.assertGreater(date(2023, 1, 1), date(2022, 12, 31))
        self.assertGreater("zebra", "aardvark")
    #    self.assertGreater(return_values(),return_values(),"True")
    #    self.assertGreater(greater_or_smaller(7,2),True)
    #    self.assertGreater(7,2,"7 is groter dan 2")

    # def test_geen_priemgetal(self):
    #     self.assertFalse(priemgetalbepalen(9))
    #     self.assertFalse(priemgetalbepalen(15))

    if __name__ == "main": unittest.main()
