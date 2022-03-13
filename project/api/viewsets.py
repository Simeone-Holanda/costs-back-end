from category.models import Category
from rest_framework import viewsets
from rest_framework.response import Response
from project.models import Project
from project.api.serializers import ProjectSerializer


# class ProjectViewSet(viewsets.ModelViewSet):
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all()

# def create(self, request, *args, **kwargs):
#     project_data = request.data

#     new_project = Project.objects.create(
#         name=project_data['name'], budget=project_data['budget'],
#         category=Category.objects.get(id=project_data['category']))
#     new_project.save()

#     serializer = ProjectSerializer(new_project)

#     return Response(serializer.data)
