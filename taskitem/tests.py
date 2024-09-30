from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from contacts.serializers import ContactSerializer
from taskitem.serializers import TaskitemSerializer

User = get_user_model()

Data = {
            "title": "dsfgdsgd",
            "description": "dsfgdgd",
            "priority": "urgent",
            "category": "User Story",
            "due_date": "2024-09-28",
            "status": "toDo",
            "contacts": [],
            "related_task": []
        }

def createTestuser():
    return User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 


class TaskItemGetTest(APITestCase):

    def test_get_taskitem_without_authentification(self):
        """
        *User is not logged in*
        *401 Error*
        """
        self.client = APIClient()     
        response = self.client.get('/api/taskitems/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_taskitem_nothing_found(self):
        """
        *User is logged in*
        *No taskitems in database found*
        """
        self.client = APIClient()  
        self.user = createTestuser()
        self.client.force_authenticate(self.user)     
     
        response = self.client.get('/api/taskitems/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_taskitem_found(self):
            """
            *User is not logged in*
            *Taskitems exists*
            """
            self.client = APIClient()  
            self.user = createTestuser()
            self.client.force_authenticate(self.user)     
            # Create a taskitem for testing
           
            serializer = TaskitemSerializer(data=Data)
            if serializer.is_valid():
                serializer.save()
        
            response = self.client.get('/api/taskitems/', format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskItemPostTest(APITestCase):

    def test_create_taskitem_without_authentification(self):
        """
        *User is not logged in*
        *401 Error*
        """
        self.client = APIClient()     
        response = self.client.post('/api/taskitems/create/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_taskitem(self):
        """
        *User is logged in*
        *Create taskitem*
        """
        self.client = APIClient()  
        self.user = createTestuser()
        self.client.force_authenticate(self.user)     

        response = self.client.post('/api/taskitems/create/', data=Data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TaskItemDetailTest(APITestCase):

    def test_taskitem_detail_without_authentification(self):
        """
        *User is not logged in*
        *401 Error*
        """
        self.client = APIClient()     
        response = self.client.get('/api/taskitems/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_taskitem_detail_get(self):
        """
        *User is logged in*
        *Get taskitem*
        """
        self.client = APIClient()  
        self.user = createTestuser()
        self.client.force_authenticate(self.user)     

         # Create a taskitem for testing
        
        serializer = TaskitemSerializer(data=Data)
        if serializer.is_valid():
            serializer.save()

        response = self.client.get('/api/taskitems/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskitem_detail_put(self):
        """
        *User is logged in*
        *Get taskitem*
        """
        self.client = APIClient()  
        self.user = createTestuser() 
        self.client.force_authenticate(self.user)     

         # Create a taskitem for testing
        
        serializer = TaskitemSerializer(data=Data)
        if serializer.is_valid():
            serializer.save()

        response = self.client.put('/api/taskitems/1/', data=Data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_taskitem_detail_delete(self):
        """
        *User is logged in*
        *Delete taskitem*
        """
        self.client = APIClient()  
        self.user = createTestuser() 
        self.client.force_authenticate(self.user)     

         # Create a taskitem for testing
        serializer = TaskitemSerializer(data=Data)
        if serializer.is_valid():
            serializer.save()

        response = self.client.delete('/api/taskitems/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)