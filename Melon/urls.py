"""
URL configuration for TenVet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from MelonApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landingPage, name="landingPage"),
    path('admin/', admin.site.urls),
    path('oNama/', views.aboutPage, name="aboutPage"),
    path('sveZivo/', views.sveZivo, name="sveZivo"),
    path('clan/', views.clan, name="clan"),
    path('clanovi/', views.members, name="members"),
    path('turniri/', views.tournaments, name="tournaments"),
    path('najave/', views.najave, name="najave"),
    path('kalendar/', views.kalendar, name="kalendar"),
    path('matchup/', views.matchup, name="matchup"),
    path('vesti/', views.vesti, name="vesti"),
    path('galerija/', views.galerija, name="galerija"),
    path('propozicije/',views.propozicije,name="propozicije"),
    path('brisanjeBodova/',views.brisanjeBodova,name="brisanjeBodova"),
    path('pravilnik/',views.pravilnik,name="pravilnik"),
    path('kategorije/',views.kategorije,name="kategorije"),
    path('opomene/',views.opomene,name="opomene"),
    path('faq/',views.faq,name="faq")
]

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
