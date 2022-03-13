from operator import mod
from django.db import models
from project.models import Project


class Service(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(blank=False, null=False)
    description = models.TextField(max_length=150)
    project = models.ForeignKey(
        Project, related_name='services', on_delete=models.CASCADE)
