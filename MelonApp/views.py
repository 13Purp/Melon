from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect


def landingPage(request):
    return render(request, 'index.html')


def aboutPage(request):

    return render(request, 'oNama.html')


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


def opomene(request):
    return None


def faq(request):
    return None
