from django.shortcuts import render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token

from taskitem.serializers import TaskitemSerializer
from .models import TaskItem

# Create your views here.
class TaskitemView(APIView):

    permission_classes = []

    def get(self, request, format=None):
        taskitems = TaskItem.objects.all()
        print(taskitems)
        serializer = TaskitemSerializer(taskitems, many=True)
        return Response(serializer.data)
