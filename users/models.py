from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
    
class UserManager(BaseUserManager):
        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('The Email field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    
        def create_superuser(self, email, password, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')
    
            return self.create_user(email, password, **extra_fields)
          
class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(unique=True, null=False, blank=False)
        first_name = models.CharField(max_length=30, null=False, blank=False)
        last_name = models.CharField(max_length=30, null=False, blank=False)
        phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits")], null=False, blank=False)
        address = models.TextField(null=True, blank=True)
        city = models.CharField(max_length=50, null=True, blank=True)
        state = models.CharField(max_length=50, null=True, blank=True)
        country = models.CharField(max_length=50, null=True, blank=True)
        pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{6}$', message="Pincode must be 6 digits")], null=True, blank=True)
        is_staff = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
        objects = UserManager()
    
        def __str__(self):
              return self.email