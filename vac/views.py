from django.shortcuts import render
from django.views import View, generic
from .forms import *
from rest_framework.views import APIView


class PatientCreateView(generic.CreateView):
    form_class = PatientCreateForm
    template_name = 'vaccination/patients/form.html'


class PatientCreateView(APIView):
    permission_classes = [

    ]

    def post(self, request):
