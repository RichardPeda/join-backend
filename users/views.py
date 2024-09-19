from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.serializers import SignupSerializer
from contacts.utils import create_default_contacts
# Create your views here.

class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
    