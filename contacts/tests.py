from django.test import Client, TestCase
from django.contrib.auth import get_user_model

from contacts.models import Contact
from rest_framework.test import APIClient, APITestCase

User = get_user_model()
class ContactTest(APITestCase):
    def test_create_contacts(self):
       
        self.client = APIClient()  

        self.user = User.objects.create_user(name='test_user', email ='test@test.de', password='test_user') 
        self.client.force_authenticate(self.user)       
    
        data = {'name': 'test_contact', 'email': 'testcontact@test.de','badge_color': '#FFFF',
                'phone': '0815', 'initials': 'TK', 'register': 'T'}
     
        response = self.client.post('/api/contacts/create/', data=data, format='json')
        self.assertEqual(response.status_code, 201)