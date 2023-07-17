from django.urls import path
from gerador_csv.views import index, gerar_csv


urlpatterns = [
    path('', index),
    path('gerar_csv', gerar_csv, name='gerar_csv'),
]
