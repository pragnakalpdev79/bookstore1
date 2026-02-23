from django.contrib import admin
from .models import LibraryUserManager,LibraryUser

@admin.register(LibraryUser)
class Libuseradmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','password')