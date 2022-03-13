from rest_framework import viewsets
from service.api import serializers
from service.models import Service


class ServiceViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ServiceSerializer
    queryset = Service.objects.all()
