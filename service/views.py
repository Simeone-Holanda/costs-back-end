from urllib import request
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from service.api.serializers import ServiceSerializer
from service.models import Service
from project.models import Project
from rest_framework.response import Response


class ServiceApiView(APIView):
    serializer_class = ServiceSerializer

    def get(self, request, id=None):
        if id != None:
            data_project = Service.objects.get(id=id)
            serializer = ServiceSerializer(data_project)
            return Response(serializer.data)

        services = Service.objects.all()
        serializer = ServiceSerializer(data=services, many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def post(self, request):
        service_data = request.data
        print(service_data)
        project = Project.objects.get(id=service_data['project'])

        new_service = Service.objects.create(name=service_data['name'],
                                             cost=service_data['cost'],
                                             description=service_data['description'],
                                             project=project,
                                             )

        project.cost = project.cost + float(new_service.cost)
        project.save()

        serializer = ServiceSerializer(new_service)

        return Response(serializer.data)

    def delete(self, request, id):
        service = get_object_or_404(Service, id=id)
        project_update = Project.objects.get(id=service.project.id)
        project_update.cost = project_update.cost - service.cost
        project_update.save()
        service.delete()
        return Response({"status": "success", "data": "Item Deleted"})


service_view = ServiceApiView.as_view()
