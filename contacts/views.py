from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token

from contacts.serializers import ContactSerializer
from .models import Contact
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from time import sleep
 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ContactView(request):
    contacts = Contact.objects.all()
    # sleep(5)
    serializer = ContactSerializer(contacts, many=True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response({'status': 'no item found'}, status=status.HTTP_404_NOT_FOUND)





    #     # contacts = Contact.objects.all()
    #     # serializer = ContactSerializer(contacts, many=True)
    #     # return Response(serializer.data)
    # def patch(self, request):
    #     print(request.data['id'])
    #     contact = Contact.objects.get(id= request.data['id'])
    #     contact.name = request.data['name']
    #     contact.save()
    #     print(contact)
    #     return Response(request.data)
        