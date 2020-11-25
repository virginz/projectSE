from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
 username = forms.EmailField()
 password = forms.CharField(widget=forms.PasswordInput)

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)