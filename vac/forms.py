from django import forms
from .models import Patient
from django.core import validators


class PatientCreateForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ['user']


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
