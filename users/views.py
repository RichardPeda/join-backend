from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.serializers import LogoutSerializer, SignupSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class SignupAPIView(CreateAPIView):
    """
    *This function register a new user.*
    """
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
def delete_guest(request):
    """
    *This function deletes a guest user.*
    *A post request check for a guest user and delete it.
    """
    try:
        user = User.objects.get(email='demo123456@mail.com', name='guest')
        user.delete()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_200_OK)
    return Response(status = status.HTTP_200_OK)
    