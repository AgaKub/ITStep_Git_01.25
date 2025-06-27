from django.contrib import admin
from .models import Produkty, Kategoria

class ProduktAdmin(admin.ModelAdmin):
    list_display =("nazwa", "cena", "czy_dostepne", "cena", "data_dodania")
    list_filter = ("czy_dostepne", "data_dodania")
    search_fields = ("nazwa", "opis")

class KategoriaAdmin(admin.ModelAdmin):
    list_display = ("nazwa", "opis")
    search_fields = ("nazwa", )

admin.site.register(Produkty, ProduktAdmin)
admin.site.register(Kategoria, KategoriaAdmin)

