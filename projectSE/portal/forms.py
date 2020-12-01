from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
 username = forms.EmailField()
 password = forms.CharField(min_length=8, widget=forms.PasswordInput)
