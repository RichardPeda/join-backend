from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from contacts.utils import create_default_contacts


# Create your views here.
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """
        *This function handles a post request for login of a registerd user.*
        *A post request returns a token, user id, email and name when the user exists.*
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        create_default_contacts(user=user.id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name' : user.name
        })