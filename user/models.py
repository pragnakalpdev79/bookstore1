from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
import uuid

# class LibraryUserManager(BaseUserManager):
#     def create_user(self,email,username=None,password=None,**extra_fields):
#         if not email:
#             raise ValueError("The email Field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email,**extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

class LibraryUser(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 350)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','first_name']
    # objects = LibraryUserManager()


