from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have and email address')
        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250, null=True)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class OTP(models.Model):
    otp = models.IntegerField()
    otp_email = models.EmailField()
    time_created = models.IntegerField()

    def __str__(self):
        return f"{self.otp_email}:{self.otp}"


