from django.urls import path
from gerador_csv.views import index, coletar_dados, adicionar_campo



urlpatterns = [
    path('', index),
    path('coletar/', coletar_dados, name='coletar_dados'),
    path('adicionar/', adicionar_campo, name='adicionar_campo'),
    path('adicionar/coletar_dados', coletar_dados, name='coletar_dados'),

]