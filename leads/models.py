from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) 
        user.set_password(password)
        user.save()

    def create_user(self,email,password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email,password,**extra_fields)



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


Source_Choice = (
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('Youtube', 'Youtube')
)

class Lead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    email = models.EmailField()
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=Source_Choice,max_length=250)
    agent = models.ForeignKey("Agent", models.SET_NULL, null=True)


class Agent(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()