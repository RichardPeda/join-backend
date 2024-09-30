from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from contacts.serializers import ContactSerializer

User = get_user_model()
class ContactGetTest(APITestCase):

    def test_get_contact_without_authentification(self):
        """
        *User is not logged in*
        *401 Error*
        """
        self.client = APIClient()     
        response = self.client.get('/api/contacts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_contact_nothing_found(self):
        """
        *User is logged in*
        *No contacts in database found*
        """
        self.client = APIClient()  
        self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
        self.client.force_authenticate(self.user)     
     
        response = self.client.get('/api/contacts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_contact_found(self):
            """
            *User is not logged in*
            *Contact exists*
            """
            self.client = APIClient()  
            self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
            self.client.force_authenticate(self.user)     
            # Create a contact for testing
            data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                    'phone': '0815', 'initials': 'TK', 'register': 'T'}
            serializer = ContactSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        
            response = self.client.get('/api/contacts/', format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class ContactPostTest(APITestCase):
    def test_create_contact_without_authentification(self):
        """
        *User is not logged in*
        *401 Error*
        """
        self.client = APIClient()     
    
        data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                'phone': '0815', 'initials': 'TK', 'register': 'T'}
     
        response = self.client.post('/api/contacts/create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_contact(self):
        """
        *User is logged in*
        *Create contact successfull*
        """
        self.client = APIClient()  
        self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
        self.client.force_authenticate(self.user)       
    
        data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                'phone': '0815', 'initials': 'TK', 'register': 'T'}
     
        response = self.client.post('/api/contacts/create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ContactDetailTest(APITestCase):
    def test_detail_contact_without_authentification(self):
        """
        *User is not logged in*
        *401 Error*
        """
        self.client = APIClient()          
        response = self.client.get('/api/contacts/1/',  format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detail_contact_get(self):
        """
        *User is logged in*
        *Get contact successfull*
        """
        self.client = APIClient()  
        self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
        self.client.force_authenticate(self.user)       
        # Create a contact for testing
        data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                    'phone': '0815', 'initials': 'TK', 'register': 'T'}
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
                serializer.save()
     
        response = self.client.get('/api/contacts/1/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_contact_put(self):
        """
        *User is logged in*
        *Updated contact successfull*
        """
        self.client = APIClient()  
        self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
        self.client.force_authenticate(self.user)       
        # Create a contact for testing
        data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                    'phone': '0815', 'initials': 'TK', 'register': 'T'}
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
                serializer.save()
     
        response = self.client.put('/api/contacts/1/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_contact_delet(self):
        """
        *User is logged in*
        *Delete contact successfull*
        """
        self.client = APIClient()  
        self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
        self.client.force_authenticate(self.user)       
        # Create a contact for testing
        data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                    'phone': '0815', 'initials': 'TK', 'register': 'T'}
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
                serializer.save()
     
        response = self.client.delete('/api/contacts/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)