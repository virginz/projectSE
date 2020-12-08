from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
 username = forms.EmailField()
 password = forms.CharField(min_length=8, widget=forms.PasswordInput)

class addSingleUserForm(forms.Form):
 email = forms.EmailField()
 password = forms.CharField(min_length=8, widget=forms.PasswordInput)
 first_name = forms.CharField()
 last_name = forms.CharField()
 usertype = forms.CharField()

class selectWeek(forms.Form):
 week = forms.IntegerField()
