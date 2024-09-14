from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token

from contacts.serializers import ContactSerializer
from .models import Contact

# Create your views here.
class ContactView(APIView):
    queryset = Contact.objects.all()
    permission_classes = []
    def get_queryset(self, *args, **kwargs):
        contacts = Contact.objects.all()
        return contacts
    def get_object(self, id):
        return get_object_or_404(self.get_queryset(), id=id)
    def get(self, request, *args, **kwargs):
        try:
            id = self.kwargs["id"]
            serializer = ContactSerializer(self.get_object(id))
        except:
            print(self)
            serializer = ContactSerializer(self.get_queryset(), many=True)

        return Response(serializer.data)





        # contacts = Contact.objects.all()
        # serializer = ContactSerializer(contacts, many=True)
        # return Response(serializer.data)
    def patch(self, request):
        print(request.data['id'])
        contact = Contact.objects.get(id= request.data['id'])
        contact.name = request.data['name']
        contact.save()
        print(contact)
        return Response(request.data)
        