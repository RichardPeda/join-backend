from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    badge_color = models.CharField(max_length=20)
    initials = models.CharField(max_length=2)
    register = models.CharField(max_length=1)
    selected = models.BooleanField(default=False)