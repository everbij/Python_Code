import unittest
from unittest.mock import patch
from unittest_examples import fahrenheit2celsius
from unittest_examples import add
from unittest_examples import divide
from unittest_examples import priemgetalbepalen
from unittest_examples import return_values
from unittest_examples import count_char
from datetime import date

class TestExamples(unittest.TestCase):

#   testen van assertAlmostEqual
    def test_fahrenheit2celsius(self): 
        print("Test met AlmostEqual")
        self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
        self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)
    
    def test_fahrenheit2celsius(self): 
        print("Test met Equal")
        self.assertAlmostEqual(fahrenheit2celsius(35), 1.6666667)
        self.assertAlmostEqual(fahrenheit2celsius(42), 5.55555556)

#   testen van assertEqual
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

#   testen van assertAlmostEqual
    def test_devide_positive_numbers(self):
        self.assertAlmostEqual(divide(2, 3),0.66667, 5)

#   testen van assertTrue en assertFalse
    def test_priemgetal(self): 
        self.assertTrue(priemgetalbepalen(7)) 
        self.assertTrue(priemgetalbepalen(17))


#   testen van assertGreater en assertLess
    def greater_or_smaller(self):
    #    print("greater or smaller")
        # result = return_values()
        # self.assertGreater(result, 12, "greater is akkoord")
        # self.assertLess(result, 12, "less is akkoord")
        # self.assertGreaterEqual(result, 12, "waarden zijn gelijk")
        self.assertGreater("raap", "aap")
    #    self.assertGreater(return_values(),return_values(),"True")
    #    self.assertGreater(greater_or_smaller(7,2),True)
    #    self.assertGreater(7,2,"7 is groter dan 2")

    # def test_geen_priemgetal(self):
    #     self.assertFalse(priemgetalbepalen(9))
    #     self.assertFalse(priemgetalbepalen(15))

    def test_addition(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(3 + 5, 8)

    @patch("unittest_examples.random.randint", return_value=7)
    def test_returns_random_integer(self, mock_randint):
        result = return_values()

        self.assertGreater(result, 5)
        mock_randint.assert_called_once_with(1, 20)

    def test_count_chars(self):
        self.assertEqual(count_char("e", "Dit is een tekst met meerdere letters e"),11)
        self.assertEqual(count_char("t", "Dit is een tekst met meerdere letters e"),6)

    if __name__ == "main": 
        unittest.main()

# tc = TestTemperatuurConversies()
# tc.greater_or_smaller()

# print(tc)
