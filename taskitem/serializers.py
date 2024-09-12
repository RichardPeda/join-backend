from rest_framework import serializers
from .models import TaskItem



class TaskitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'