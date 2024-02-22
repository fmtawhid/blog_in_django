from django import forms
from .models import article,auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class createForm(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            'title',
            'body',
            'image',
            'catagory',
        ]


class Usercreate(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]
        

class createAuthor(forms.ModelForm):
    class Meta:
        model = auth
        fields = [
            'image',
            'details'
        ]
