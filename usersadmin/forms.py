from django import forms


class GroupForm(forms.ModelForm):

    class Meta:
        fields = [
            "name",
        ]
