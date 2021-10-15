from django import forms
from .models import Patient
from django.core import validators
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ['role']


class PatientCreateForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields= '__all__'
