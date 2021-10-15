from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import *


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class DistrictSerializer(ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class CentreSerializer(ModelSerializer):

    class Meta:
        model = Centre
        fields = '__all__'
