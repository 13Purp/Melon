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
from django.urls import include, path
from MelonApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include('MelonApp.api_urls')),
    path('<int:promo_id>', views.get_promo_details, name='get_promo_details'),
    path('', views.landingPage, name="landingPage"),
    path('admin/', admin.site.urls),
    path('oNama/', views.aboutPage, name="aboutPage"),
    path('dodajPopust/', views.dodajPopust, name="dodajPopust"),
    path('sveZivo/', views.sveZivo, name="sveZivo"),
    path('clan/', views.clan, name="clan"),
    path('vesti/', views.vesti, name="vesti"),
    path('login/', views.loginPage, name="login"),
    path('stats/',views.stats, name="stats"),

    path('statistics/<int:store_id>/', views.get_top_transitions, name='statistics'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
