from django import forms

from channels.models import Community


class CommunityPostForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ["title", "image", "content"]
