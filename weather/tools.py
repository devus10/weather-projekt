# -*- coding: utf-8 -*-
import pyowm
import json
import re


class OperacjePogody:
    OWM = pyowm.OWM('64ad2a7c86d09f369976e3acd3007e04')

    def aktualna_pogoda_miasto(self, city_name):
        observation = self.OWM.weather_at_place(city_name)
        return observation.get_weather().to_JSON()

    def aktualna_pogoda_wspolrzedne(self, lat, lon):
        observation_list = self.OWM.weather_at_coords(lat, lon)
        return observation_list.get_weather().to_JSON()

    def prognoza_pogody_miasto(self, city_name, days):
        forecast_for_few_days = self.OWM.daily_forecast(city_name, days)
        weathers = forecast_for_few_days.get_forecast().get_weathers()

        for weather in weathers:
            print weather.get_reference_time('iso'), weather.to_JSON()

    def get_temperatura(self, weatherJSON):
        weather = json.loads(weatherJSON)
        return weather['temperature']['temp']

    def get_wilgotnosc(self, weatherJSON):
        weather = json.loads(weatherJSON)
        return weather['humidity']

    def get_zachmurzenie(self, weatherJSON):
        weather = json.loads(weatherJSON)
        return weather['clouds']

    def get_cisnienie(self, weatherJSON):
        weather = json.loads(weatherJSON)
        return weather['pressure']['press']

class KonwerterTemperatur:

    @staticmethod
    def przelicz_na_celsjusz(kelwin):
        celsjusz = float(kelwin) - 273
        return int(celsjusz)

class SprawdzanieTypu:

    @staticmethod
    def sprawdzCzyKonwertowalnyNaFloat(input):
        if re.match("^\d+?\.\d+?$", input) is None:
            return False
        else:
            return True

    @staticmethod
    def sprawdzCzyKonwertowalnyNaInt(input):
        try:
            int(input)
            return True
        except ValueError:
            return False

op = OperacjePogody()



# print op.get_zachmurzenie(op.aktualna_pogoda_miasto('London'))
# print op.get_cisnienie(op.aktualna_pogoda_miasto('London'))
# print op.get_wilgotnosc(op.aktualna_pogoda_miasto('London'))
# print SprawdzanieTypu.sprawdzCzyKonwertowalnyNaFloat("50.01")
# print SprawdzanieTypu.sprawdzCzyKonwertowalnyNaInt("50.01")
