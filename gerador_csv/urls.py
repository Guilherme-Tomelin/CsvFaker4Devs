from django.urls import path
from gerador_csv.views import index


urlpatterns = [
    path('', index),
]