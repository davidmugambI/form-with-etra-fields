from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import ZalegoDet
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    GENDER_CHOICES = (
        ('male', "male"),
        ('female', 'female'),

    )
    LANGUAGE_CHOICES =(
        ('java', 'java'),
        ('c','c'),
        ('python','python'),
    )
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    lang = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=True)
    image = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','gender', 'image','lang', 'username','password1', 'password2',)

