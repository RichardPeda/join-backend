from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token

from contacts.serializers import ContactSerializer
from .models import Contact
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_contacts(request):
    """
    *This function returns all existing contacts when a get request is sent.*
    *If no contacts are found the function returns a 404 error.*
    """
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    if serializer.data:
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'no item found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_contact(request):
    """
    *This function creates a new contact when a post request is sent.*
    *If the contact is successfully created, the function returns a 201 status.*
    *If the contact clouldn´t be created, the function returns a 400 error.*
    """
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contact_detail(request, pk):
    """
    *This function handles a get, put or delete request on a contact with a given primary key.*
    *A get request returns the contact with the primary key.*
    *A put request updates the contact and returns it.*
    *A delete request deletes the contact and returns a 204 status.*
    """
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        