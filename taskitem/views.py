from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token
from rest_framework import status
from taskitem.serializers import SubtaskSerializer, TaskitemSerializer
from .models import SubtaskItem, TaskItem
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    """
    *This function returns all existing tasks.*
    *A get request returns all task when they exists, otherwise a 404 error is returned.*
    """
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
    """
    *This function creates a new task.*
    *A post request creates a new task and returns a the data and a 204 status.*
    *When the task couldn´t be created a 400 status is returned.*
    """
    print(request.data)
    serializer = TaskitemSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    """
    *This function returns, update or delete a task with a primary key.*
    *A get request returns a task when found, otherwise a 404 error*
    *A put request updates a task and returns the data when the data is valid, otherwise a 400 error.*
    *A delete request deletes a task and returns a 204 status.*
    """
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

@api_view(['PUT'])
def task_status(request, pk):
    """
    *This function updates the task status with a primary key.*
    *A put request updates a task status and returns the data when the data is valid, otherwise a 400 error.*
    """
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
    """
    *This function creates a subtask.*
    *A Post request creates a subtask with the data when valid and returns the data and a 201 status.*
    *Invalid data returns a 400 error*
    """
    serializer = SubtaskSerializer(data=request.data, many=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_subtask(request, pk):
    """
    *This function change the subtask checked status with a primary key.*
    *A put request updates a subtask checked status and returns the data when the data is valid, otherwise a 400 error.*
    """
    try:
        subtask = SubtaskItem.objects.get(pk=pk)
    except SubtaskItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SubtaskSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)









# class TaskitemDetailView(APIView):
#     def get(self, request, id=None):
#         print(id)
#         task = TaskItem.objects.filter(id=id)
#         if task:
#             task_serializer = TaskitemSerializer(task, many=True)
#             return Response(task_serializer.data)
#         else:
#             # return Response({'error': 'no item'})
#             return Response({'status': 'no item found'}, status=status.HTTP_404_NOT_FOUND)
