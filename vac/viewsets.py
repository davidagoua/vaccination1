from rest_framework.viewsets import ModelViewSet
from . import serializers
from .models import *


class PatientViewset(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class VaccinViewset(ModelViewSet):
    queryset = Vaccin.objects.all()
    serializer_class = serializers.VaccinSerializer


class VaccinationViewset(ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = serializers.VaccinationSerializer


class TestSeroViewset(ModelViewSet):
    queryset = TestSero.objects.all()
    serializer_class = serializers.TestSeroSerializer


class EnquetViewset(ModelViewSet):
    queryset = Enquete.objects.all()
    serializer_class = serializers.EnqueteSerializer
