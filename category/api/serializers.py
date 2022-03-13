from rest_framework import serializers
from category import models


class CategorySerializer(serializers.ModelSerializer):

    
    class Meta():
        model = models.Category
        fields = '__all__'
