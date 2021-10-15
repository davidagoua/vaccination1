from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user','code','state']


@admin.register(Vaccin)
class VaccinAdmin(admin.ModelAdmin):
    list_display = ['nom','actif','exp']


@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ['vaccin','patient','agent']


@admin.register(TestSero)
class TestSeroAdmin(admin.ModelAdmin):
    list_display = ['patient','datetest','igg','igm']


@admin.register(Enquete)
class Enquete(admin.ModelAdmin):
    list_display = ['patient','positifcov','maladies','signeclinique']

