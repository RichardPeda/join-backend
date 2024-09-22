from rest_framework import serializers
from .models import SubtaskItem, TaskItem
from contacts.serializers import ContactSerializer


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtaskItem
        fields = '__all__'

class TaskitemSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    related_task = SubtaskSerializer(source='subtask_item_set', many=True)
    class Meta:
        model = TaskItem
        fields = ['id','title','description','priority','category','due_date','status','contacts', 'related_task']