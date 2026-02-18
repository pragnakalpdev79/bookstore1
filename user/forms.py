from django import forms
from .models import LibraryUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re,os

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ['first_name','last_name','email']
        #email = forms.EmailField(required=True)
        # widgets = {
        #     'password': forms.PasswordInput(),
        # }
    def clean(self):
        os.system('clear')
        data = self.cleaned_data
        mail = data.get('email')
        if not mail:
            raise ValidationError("Please enter the mail")
        regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
        print(data,mail)
        validmail = re.match(regex,mail)
        if not validmail:
            raise ValidationError("test sucess")
        if data.get('password1') != data.get('password2'):
            raise ValidationError("Passworrd does not match!")
        return data

        

