from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['alias', 'email']
