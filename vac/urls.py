from django.urls import path
from .views import *
from .apps import VacConfig


app_name = VacConfig.name

urlpatterns = [
    path('patient/create/', PatientCreateView.as_view(), name='patient_create'),
]