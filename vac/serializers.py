from rest_framework.serializers import ModelSerializer
from . import models


class PatientSerializer(ModelSerializer):

    class Meta:
        model = models.Patient
        fields = '__all__'


class VaccinSerializer(ModelSerializer):

    class Meta:
        model = models.Vaccin
        fields = '__all__'


class VaccinationSerializer(ModelSerializer):

    class Meta:
        model = models.Vaccination
        fields = '__all__'


class TestSeroSerializer(ModelSerializer):

    class Meta:
        model = models.TestSero
        fields = '__all__'


class EnqueteSerializer(ModelSerializer):

    class Meta:
        model = models.Enquete
        fields = '__all__'

