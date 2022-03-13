from functools import partial
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response
from project.models import Project
from category.models import Category
from service.models import Service
from project.api.serializers import ProjectSerializer
from django.shortcuts import get_object_or_404


class ProjectsApiView(APIView):
    serializer_class = ProjectSerializer

    def get(self, request, id=None):
        if(id != None):
            data_project = Project.objects.get(id=id)
            serializer = ProjectSerializer(data_project)
            return Response(serializer.data)

        data_project = Project.objects.all()
        serializer = ProjectSerializer(data=data_project, many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def post(self, request):
        project_data = request.data

        new_project = Project.objects.create(
            name=project_data['name'], budget=project_data['budget'],
            category=Category.objects.get(id=project_data['category']),
            cost=project_data['cost'])

        new_project.save()

        serializer = ProjectSerializer(new_project)

        return Response(serializer.data)

    def put(self, request, id):
        project_data = request.data

        new_project = Project.objects.get(id=id)

        new_project.name = project_data['name']
        new_project.budget = project_data['budget']
        new_project.category = Category.objects.get(
            id=project_data['category'])
        new_project.cost = project_data['cost']
        new_project.save()

        serializer = ProjectSerializer(new_project, project_data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    # def patch(self, request, id):
    #     project = Project.objects.get(id=id)
    #     # category =
    #     # set partial=True to update a data partially
    #     print(request.data)
    #     serializer = ProjectSerializer(project, request.data, partial=True)
    #     if serializer.is_valid():
    #         print('passou')
    #         serializer.save()
    #         print(serializer.data)
    #     return Response(serializer.data)

    def delete(self, request, id):
        project = get_object_or_404(Project, id=id)
        project.delete()
        return Response({"status": "success", "data": "Item Deleted"})


project_view = ProjectsApiView.as_view()
