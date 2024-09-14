from rest_framework import serializers
from .models import Subtask_item, TaskItem
from contacts.serializers import ContactSerializer


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask_item
        fields = '__all__'

class TaskitemSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    related_task = SubtaskSerializer(source='subtask_item_set', many=True)
    class Meta:
        model = TaskItem
        # fields = '__all__',
        # fields = ['id','contacts' 'rel_task']
        fields = ['id','title','description','priority','status','contacts', 'related_task']