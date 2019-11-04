from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ImageField
from .models import UserProfile, Our_User


class ProfileForm(forms.ModelForm):
    """
    Django based Form for accepting user_type, user address, user picture  for user creation
    """
     class Meta:
         model = Our_User
         fields = ('user_type', 'address', 'picture')


class UserForm(forms.ModelForm):
    """
    Django based form for accepting username, email and password for user creation
    """
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
