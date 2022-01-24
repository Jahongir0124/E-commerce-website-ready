from django import forms
from django.forms import ModelForm
from .models import Products,User
from django.contrib.auth.forms import UserCreationForm
class ProductForm(ModelForm):
    class Meta:
        model=Products
        fields='__all__'
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
class Login(forms.Form):
    username=forms.CharField(label="User Name",max_length=100)
    password=forms.CharField(label="Password",max_length=200)
