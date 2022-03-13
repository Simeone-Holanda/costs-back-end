import imp
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from category.api import viewsets as categoryviewset
from project.views import project_view
from service.views import service_view
from service.api import viewset as serviceviewset

route = routers.DefaultRouter()
route.register(r'categories', categoryviewset.CategoryViewSets,
               basename="Category")
# route.register(r'services', serviceviewset.ServiceViewSets,
#                basename="Service")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', project_view),
    path('projects/<int:id>', project_view),
    path('services/', service_view),
    path('services/<int:id>', service_view),
    path('', include(route.urls)),
]
