from django.urls import path
from .api_views import ProveriPopustView, IzvrsiTransakcijuView

app_name = 'api'

urlpatterns = [
    path('check', ProveriPopustView.as_view(), name='proveri_popust'),
    path('transaction', IzvrsiTransakcijuView.as_view(), name='izvrsi_transakciju'),
]
