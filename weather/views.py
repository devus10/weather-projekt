from django.shortcuts import render
from django.http import HttpResponse
from tools import OperacjePogody, KonwerterTemperatur, SprawdzanieTypu


def index(request):
    return render(request, 'weather/index.html', )


def popup_miasto(request):
    miasto = request.POST.get("miasto", "")

    operacjePogody = OperacjePogody()
    pogoda = operacjePogody.aktualna_pogoda_miasto(miasto)

    temperatura = KonwerterTemperatur.przelicz_na_celsjusz(operacjePogody.get_temperatura(pogoda))
    wilgotnosc = operacjePogody.get_wilgotnosc(pogoda)
    zachmurzenie = operacjePogody.get_zachmurzenie(pogoda)
    cisnienie = operacjePogody.get_cisnienie(pogoda)

    return render(request, 'weather/miasto.html', {'miasto': miasto, 'temperatura': temperatura
        , 'wilgotnosc': wilgotnosc, 'zachmurzenie': zachmurzenie,
                                                   'cisnienie': cisnienie})


def popup_wspolrzedne(request):
    lat_otrzymany = request.POST.get("lat", "")
    lon_otrzymany = request.POST.get("lon" "")

    lat = None
    lon = None
    if(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaInt(lat_otrzymany) and SprawdzanieTypu.sprawdzCzyKonwertowalnyNaInt(lon_otrzymany)):
        bledne_dane = False
        lat = float(lat_otrzymany)
        lon = float(lon_otrzymany)
    elif(SprawdzanieTypu.sprawdzCzyKonwertowalnyNaFloat(lat_otrzymany) and SprawdzanieTypu.sprawdzCzyKonwertowalnyNaFloat(lon_otrzymany)):
        bledne_dane = False
        lat = float(lat_otrzymany)
        lon = float(lon_otrzymany)
    else:
        bledne_dane = True
        return render(request, 'weather/wspolrzedne.html', {'bledne_dane': bledne_dane})

    operacjePogody = OperacjePogody()
    pogoda = operacjePogody.aktualna_pogoda_wspolrzedne(lat, lon)

    temperatura = KonwerterTemperatur.przelicz_na_celsjusz(operacjePogody.get_temperatura(pogoda))
    wilgotnosc = operacjePogody.get_wilgotnosc(pogoda)
    zachmurzenie = operacjePogody.get_zachmurzenie(pogoda)
    cisnienie = operacjePogody.get_cisnienie(pogoda)

    return render(request, 'weather/wspolrzedne.html', {'lat': lat, "lon": lon,
                                                        'temperatura': temperatura
        , 'wilgotnosc': wilgotnosc, 'zachmurzenie': zachmurzenie,
                                                        'cisnienie': cisnienie, 'bledne_dane': bledne_dane})
