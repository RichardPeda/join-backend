from django.shortcuts import render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token

from contacts.serializers import ContactSerializer
from .models import Contact

# Create your views here.
class ContactView(APIView):

    permission_classes = []

    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)