from contacts.serializers import ContactSerializer
from users.serializers import User
from .models import Contact




contact_1 ={
          "badge_color": '#1FD7C1',
          "initials": 'RS',
          "register": 'R',
          "name": 'Rainer Sonnenschein',
          "email": 'sonnenschein@draussen.de',
          "phone": '+49 30 5678 9456',
          "selected": False,
        }

contact_2    =    {
          "badge_color": '#00BEE8',
          "initials": 'PN',
          "register": 'P',
          "name": 'Pia Nist',
          "email": 'musikerin@mitherz.de',
          "phone": '+49 221 3456412',
          "selected": False,
        }

contact_3 =        {
          "badge_color": '#FFA35E',
          "initials": 'AF',
          "register": 'A',
          "name": 'Arne Fröhlich',
          "email": 'froehlich@24-7.com',
          "phone": '+49 815 79183212',
          "selected": False,
        }

contact_4 =        {
          "badge_color": '#FFA35E',
          "initials": 'KE',
          "register": 'K',
          "name": 'Karl Ender',
          "email": 'karlender@datum.com',
          "phone": '+49 711 3652987',
          "selected": False,
        }

contact_5 = {
          "badge_color": '#FF745E',
          "initials": 'KH',
          "register": 'K',
          "name": 'Klara Himmel',
          "email": 'gerne@sommer.de',
          "phone": '+49 123 456 789',
          "selected": False,
        }
contact_6 = {       
          "badge_color": '#00BEE8',
          "initials": 'CK',
          "register": 'C',
          "name": 'Christiane Krise',
          "email": 'krise@serveranbindung.de',
          "phone": '+49 221 3456413',
          "selected": False,
        }

contact_7 = {
          "badge_color": '#FF7A00',
          "initials": 'JD',
          "register": 'J',
          "name": 'John Doe',
          "email": 'john.doe@example.com',
          "phone": '835769376',
          "selected": False,
        }

contact_8 = {       
          "badge_color": '#FF5EB3',
          "initials": 'AS',
          "register": 'A',
          "name": 'Alice Smith',
          "email": 'alice.smith@example.com',
          "phone": '835769377',
          "selected": False,
        }

contact_9 =  {
       
          "badge_color": '#6E52FF',
          "initials": 'MP',
          "register": 'M',
          "name": 'Michael Phillips',
          "email": 'michael.phillips@example.com',
          "phone": '835769378',
          "selected": False,
        }

contact_10 = {
        
          "badge_color": '#9327FF',
          "initials": 'EK',
          "register": 'E',
          "name": 'Emily King',
          "email": 'emily.king@example.com',
          "phone": '835769379',
          "selected": False,
        }


def create_default_contacts(user):
    serializer = ContactSerializer(data=contact_1)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_2)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_3)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_4)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_5)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)
    
    serializer = ContactSerializer(data=contact_6)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_7)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_8)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_9)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)

    serializer = ContactSerializer(data=contact_10)
    if(serializer.is_valid(raise_exception=True)):
       serializer.create(serializer.data)
   






  