from django.contrib import admin
from gerador_csv.models import Informacao

class ListaInformacao(admin.ModelAdmin):
    list_display = ("id", "tipo_informacao", "categoria")
    list_display_links = ("id",)
    search_fields = ("id", "tipo_informacao", "categoria")
    list_filter = ("id", "tipo_informacao")
    list_per_page = 35

admin.site.register(Informacao, ListaInformacao)
