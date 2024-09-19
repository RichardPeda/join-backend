from django.db import models
from django.conf import settings

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    badge_color = models.CharField(max_length=20)
    initials = models.CharField(max_length=2)
    register = models.CharField(max_length=1)
    selected = models.BooleanField(default=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'({self.id}) {self.name}'