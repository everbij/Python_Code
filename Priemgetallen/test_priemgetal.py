# Gebruiker@TALENTCLASS064 MINGW64 /c/TC_Python/Priemgetallen
# $ python -m unittest -v test_priemgetal.py
import unittest 
from priemgetal import priemgetalbepalen # te testen methode in programma priemgetal

class TestPriemgetal(unittest.TestCase):

    def test_priemgetal(self): 
        # testen waarbij de verstrekte waarde een priemgetal is
        # vandaar de assertTrue als methode
        # de waarde die meegegeven wordt staat tussen de ()
        self.assertTrue(priemgetalbepalen(2)) 
        self.assertTrue(priemgetalbepalen(7)) 
        self.assertTrue(priemgetalbepalen(17))
        self.assertTrue(priemgetalbepalen(23))
        self.assertTrue(priemgetalbepalen(31))

    def test_geen_priemgetal(self):
        # testen waarbij de verstrekte waarde geen priemgetal is
        # vandaar de assertFalse als methode
        # de waarde die meegegeven wordt staat tussen de ()
        self.assertFalse(priemgetalbepalen(9))
        self.assertFalse(priemgetalbepalen(15))
        self.assertFalse(priemgetalbepalen(27))

if __name__ == "main": unittest.main()