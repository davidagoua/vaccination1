from django.shortcuts import render
from django.views import View, generic
from .forms import *
from rest_framework.views import APIView


class PatientCreateView(View):

    def get(self, request, *args, **kwargs):
        user_form = UserCreateForm
        patient_form = PatientCreateForm
        return render(request, 'vac/patient_create.html', locals())

    def post(self, request, *args, **kwargs):
        user_form = UserCreateForm(request.POST, request.FILES)
        patient_form = PatientCreateForm()
