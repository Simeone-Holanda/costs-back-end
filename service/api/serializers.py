from rest_framework import serializers
from service import models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Service
        fields = '__all__'
