from django.contrib import admin
from .models import Currency, SectorChoice, Country

admin.site.register(Currency)
admin.site.register(SectorChoice)
admin.site.register(Country)
