from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework.decorators import api_view
 

from .serializers import ProjectSerializer
from .models import Project
 
# create a class for the Todo model viewsets

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
 
    queryset = Project.objects.all()