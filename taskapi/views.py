from django.shortcuts import render
from rest_framework import viewsets
from taskapi.models import TaskManager
from taskapi.serializers import managingserializer



# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskManager.objects.all()
    serializer_class = managingserializer

