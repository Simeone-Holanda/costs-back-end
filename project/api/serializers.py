from rest_framework import serializers
from project import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Project
        fields = ['id', 'name', 'budget', 'cost', 'category', 'services']
        depth = 1
