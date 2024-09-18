from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from uuid import uuid4
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, name, **extra_fields):
        if not email:
            raise ValueError()
        user = self.model(email = self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,name, email, password):
        user = self.create_user(email=email, password=password, name=name)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, default='')
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]
    objects = UserManager()
