from django import forms

from channels.models import Community
from videos.models import Video


class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'title', 'onkeyup': 'titleValidate()'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'file'}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class': 'file'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'id': 'description', 'onkeyup': 'desc_validate()'}))
    # tags = forms.CharField(widget=forms.TextInput(attrs={'id': 'tags', 'onkeyup': 'desc_validate()'}))

    class Meta:
        model = Video
        fields = ['video', 'image', 'title', 'description', 'tags', 'visibilty']
