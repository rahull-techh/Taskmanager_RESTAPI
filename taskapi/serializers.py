from rest_framework import serializers
from .models import TaskManager

class managingserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskManager
        fields = "__all__"