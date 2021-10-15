from rest_framework import viewsets, permissions
from . import serializers
from .models import User, Centre, District


class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]


class CentreViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CentreSerializer
    queryset = Centre.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]


class DistrictViewset(viewsets.ModelViewSet):
    serializer_class = serializers.DistrictSerializer
    queryset = District.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
