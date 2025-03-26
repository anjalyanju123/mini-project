from django import forms
from .models import *
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm, AuthenticationForm

# User Registration Form (with password confirmation)
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    

# User Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'address', 'phone', 'age', 'upload']


class PasswordResetForm(PasswordChangeForm):
    old_password = None  # We don’t need the old password here        