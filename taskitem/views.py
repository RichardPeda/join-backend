from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token
from rest_framework import status
from taskitem.serializers import TaskitemSerializer
from .models import TaskItem
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TaskitemView(request):

    taskitems = TaskItem.objects.all()
    serializer = TaskitemSerializer(taskitems, many=True)
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
