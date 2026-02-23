from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class LibraryUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError(_('The email field must be set'))
        email = self.normalize_email(email)
      git  user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        
        return self.create_user(email,password,**extra_fields)

class LibraryUser(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 350)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    #can_buy_book = models.BooleanField(default=False)
    #can_add_book = models.BooleanField(default=False)
    objects = LibraryUserManager()
    class Meta:
        permissions = [
            ('can_add_book',"To let sellers add new products"),
            ("can_buy_book","To let only normal users buy books")
        ]


