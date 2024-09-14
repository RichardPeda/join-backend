from django.shortcuts import get_object_or_404, render
from rest_framework.authtoken.views import APIView, ObtainAuthToken, Response, Token

from taskitem.serializers import TaskitemSerializer
from .models import TaskItem

# Create your views here.
class TaskitemView(APIView):

    permission_classes = []
    def get_queryset(self, *args, **kwargs):
        contacts = TaskItem.objects.all()
        return contacts
    def get_object(self, id):
        return get_object_or_404(self.get_queryset(), id=id)
    def get(self, request, *args, **kwargs):
        try:
            id = self.kwargs["id"]
            serializer = TaskitemSerializer(self.get_object(id))
        except:
            print(self)
            serializer = TaskitemSerializer(self.get_queryset(), many=True)

        return Response(serializer.data)
    
