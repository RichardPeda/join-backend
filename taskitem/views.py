from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token
from rest_framework import status
from taskitem.serializers import TaskitemSerializer
from .models import TaskItem

# Create your views here.
class TaskitemView(APIView):

    permission_classes = []
    def get_queryset(self, *args, **kwargs):
        contacts = TaskItem.objects.all()
        return contacts
   
    def get(self, request, *args, **kwargs):
            serializer = TaskitemSerializer(self.get_queryset(), many=True)
            if serializer.data:
                return Response(serializer.data)
            else:
                return Response({'status': 'no item found'}, status=status.HTTP_404_NOT_FOUND)

class TaskitemDetailView(APIView):
    def get(self, request, id=None):
        print(id)
        task = TaskItem.objects.filter(id=id)
        if task:
            task_serializer = TaskitemSerializer(task, many=True)
            return Response(task_serializer.data)
        else:
            # return Response({'error': 'no item'})
            return Response({'status': 'no item found'}, status=status.HTTP_404_NOT_FOUND)
