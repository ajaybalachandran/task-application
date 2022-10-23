from django import forms
from django.contrib.auth.models import User
from task.models import Task


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control border border-primary", "placeholder": "Enter Username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control border border-primary",  "placeholder": "Enter Password"}))


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'status']
        
