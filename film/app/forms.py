from django import forms
from .models import Movies


class Form(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'desc', 'img']
