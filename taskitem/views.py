from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token
from rest_framework import status
from taskitem.serializers import SubtaskSerializer, TaskitemSerializer
from .models import TaskItem
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_tasks(request):

    taskitems = TaskItem.objects.all()
    serializer = TaskitemSerializer(taskitems, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response({'status': 'no item found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_task(request):
    print(request.data)
    serializer = TaskitemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def task_detail(request, pk):
    try:
        task = TaskItem.objects.get(pk=pk)
        print(task)
    except TaskItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskitemSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(request.data)
        serializer = TaskitemSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    print(request.data)
    serializer = TaskitemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_status(request, pk):
    try:
        task = TaskItem.objects.get(pk=pk)
    except TaskItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TaskitemSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_subtask(request):
    print(request.data)
    # rel_id = request.data['rel_task']
    # task = TaskItem.objects.get(pk=rel_id)

    serializer = SubtaskSerializer(data=request.data, many=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
