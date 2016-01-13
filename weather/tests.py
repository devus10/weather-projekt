from django.test import TestCase
import unittest, json
from tools import KonwerterTemperatur, OperacjePogody, SprawdzanieTypu

class TestyJednostkowe(unittest.TestCase):
    operacjePogody = OperacjePogody()

    def test_konwertera_temperatur(self):
        kelwin = 273
        celsjusz = 0
        self.assertEqual(KonwerterTemperatur.przelicz_na_celsjusz(kelwin), celsjusz)

    def test_string_na_float(self):
        string_int = "5"
        string_float = "5.0"
        string_random = "xyz123.5"
        self.assertFalse(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaFloat(string_int))
        self.assertTrue(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaFloat(string_float))
        self.assertFalse(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaFloat(string_random))

    def test_string_na_int(self):
        string_int = "5"
        string_float = "5.0"
        string_random = "xyz123.5"

        self.assertTrue(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaInt(string_int))
        self.assertFalse(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaInt(string_float))
        self.assertFalse(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaInt(string_random))

    def test_get_temperatura(self):
        miasto = 'London'
        pogoda_miasto = self.operacjePogody.aktualna_pogoda_miasto(miasto)
        temperatura = self.operacjePogody.get_temperatura(pogoda_miasto)

        czy_jest_float = type(temperatura) is float
        self.assertTrue(czy_jest_float)

    def test_get_wilgotnosc(self):
        miasto = 'London'
        pogoda_miasto = self.operacjePogody.aktualna_pogoda_miasto(miasto)
        wilgotnosc = self.operacjePogody.get_wilgotnosc(pogoda_miasto)

        czy_jest_int = type(wilgotnosc) is int
        self.assertTrue(czy_jest_int)

    def test_get_zachmurzenie(self):
        miasto = 'London'
        pogoda_miasto = self.operacjePogody.aktualna_pogoda_miasto(miasto)
        zachmurzenie = self.operacjePogody.get_zachmurzenie(pogoda_miasto)

        czy_jest_int = type(zachmurzenie) is int
        self.assertTrue(czy_jest_int)

    def test_get_cisnienie(self):
        miasto = 'London'
        pogoda_miasto = self.operacjePogody.aktualna_pogoda_miasto(miasto)
        cisnienie = self.operacjePogody.get_cisnienie(pogoda_miasto)

        czy_jest_int = type(cisnienie) is int
        self.assertTrue(czy_jest_int)




if __name__ == '__main__':
    unittest.main()



# Create your tests here.
