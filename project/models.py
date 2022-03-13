from codecs import backslashreplace_errors
from django.db import models
from category.models import Category


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    budget = models.FloatField(null=False, blank=False)
    cost = models.FloatField(null=False, blank=False, default=0)
    category = models.ForeignKey(
        Category, related_name='projects', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
