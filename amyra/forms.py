from django import forms

from .models import Files


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file', )
