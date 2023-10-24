from django import forms
from .models import User, Group
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select, FileInput, HiddenInput


class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'group']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'user08'}),
            'group': forms.Select(attrs={'class': 'form-control mt-3'}),
        }


class CreateGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Name of group'}),
            'description': forms.TextInput(attrs={'class': 'form-control mt-3'}),
        }