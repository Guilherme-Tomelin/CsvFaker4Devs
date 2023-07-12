from django.urls import path
from gerador_csv.views import index, coletar_dados



urlpatterns = [
    path('', index),
    path('coletar/', coletar_dados, name='coletar_dados'),
]