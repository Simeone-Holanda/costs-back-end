from rest_framework import viewsets
from category.api import serializers
from category import models


class CategoryViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
