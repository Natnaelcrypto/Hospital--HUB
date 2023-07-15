
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class HospitalForm(ModelForm):
    class Meta:
        model=Hospital
        fields=["name","description","address"]
    

class LoginForm(AuthenticationForm):
    
    class Meta:
        model=User
        fields=['username','password']

    username = forms.CharField(widget=forms.TextInput(attrs={
         "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Your username",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Your password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

class SignupForm(UserCreationForm):

    class Meta():
        model=User
        fields=('username', 'email', 'password1',"password2","role")

    username = forms.CharField(widget=forms.TextInput(attrs={
         "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Your username",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
         "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Your email",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Your password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

    ROLE_CHOICES = (
        ('HM', 'Hospital Manager'),
        ('GU', 'Guest'),
    )

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={
        "class": "w-100 px-2",
        "required": "true",
        "style": "border-radius: 5px; border: none; height: 35px",
        "id":"role"
    }))

class AppointmentForm(ModelForm):
    class Meta():
        models=Appointment
        fields=fields = ['hospital', 'first_name',"last_name", 'age', 'service_id', 'gender']

    hospital=forms.CharField(widget=forms.TextInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

    last_name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))

    Gender_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    age=forms.CharField(widget=forms.Select(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    },choices=Gender_CHOICES))

    service_id=forms.CharField(widget=forms.Select(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))
    hospital=forms.CharField(widget=forms.TextInput(attrs={
        "class":"w-100 px-2",
                "required":"true",
                "placeholder":"Repeat password",
                 "style":"border-radius: 5px; border: none; height: 35px"
    }))
    
