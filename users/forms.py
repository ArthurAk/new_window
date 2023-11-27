from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'validate',
        'id': 'reg_user_name',
        'onkeyup': 'validate()'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'validate',
        'id': 'reg_user_name',
        'onkeyup': 'validate()'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': '',
        'id': 'reg_pass_word',
        'onkeyup': 'validate()'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': '',
        'id': 'reg_pass_word',
        'onkeyup': 'validate()'
    }))

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class UserLoginForm(forms.Form):
    pass