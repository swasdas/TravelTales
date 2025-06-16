from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post # this will import Post class from models.py
        fields = ['title','body','url_key','banner']
        