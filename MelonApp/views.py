from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Sadrzaj
def landingPage(request):
    return render(request,'index.html')


def aboutPage(request):
    return render(request,'oNama.html')


def sveZivo(request):
    return render(request, 'landingPage.html')


def clan(request):
    return render(request, 'pregledClana.html')


def members(request):
    return None


def tournaments(request):
    return None


def matchup(request):
    return render(request, 'matchupTree.html')


def vesti(request):
    return render(request, 'vesti.html')


def najave(request):
    return render(request, 'vesti.html')


def kalendar(request):
    return render(request, 'vesti.html')


def galerija(request):
    return None


def propozicije(request):
    sadrzaj = Sadrzaj.objects.get(putanja='/propozicije')
    html_page_data = {
        'content': sadrzaj.tekst
    }
    return render(request, 'propozicije.html',html_page_data)


def brisanjeBodova(request):
    sadrzaj = Sadrzaj.objects.get(putanja='/brisanjeBodova')
    html_page_data = {
        'content': sadrzaj.tekst
    }
    return render(request, 'brisanjeBodova.html', html_page_data)


def pravilnik(request):
    sadrzaj = Sadrzaj.objects.get(putanja='/pravilnik')
    html_page_data = {
        'content': sadrzaj.tekst
    }
    return render(request, 'pravilnik.html', html_page_data)


def kategorije(request):
    sadrzaj = Sadrzaj.objects.get(putanja='/kategorije')
    html_page_data = {
        'content': sadrzaj.tekst
    }
    return render(request, 'kategorije.html', html_page_data)


def opomene(request):
    return None


def faq(request):
    return None