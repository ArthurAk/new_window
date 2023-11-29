from django import forms

from users.models import Permission


class GroupForm(forms.ModelForm):

    class Meta:
        fields = [
            "name",
        ]


class PermissionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'placeholder': 'Enter Name'}))
    codename = forms.CharField(widget=forms.TextInput(attrs={'id': 'codename', 'class': 'form-control', 'placeholder': 'Enter Code Name'}))

    class Meta:
        model = Permission
        fields = [
            "name",
            "codename"
        ]
