from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import User
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select, FileInput, HiddenInput
from .models import Group


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'group']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'user08'}),
            'group': forms.Select(attrs={'class': 'form-control mt-3'}),
        }
