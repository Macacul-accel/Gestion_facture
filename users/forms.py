from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "password")

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'email', 'phone_number',)

class LogInForm(forms.Form):
    adresse_mail = forms.CharField()
    mot_de_passe = forms.CharField(widget=forms.PasswordInput)
