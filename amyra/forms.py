from django import forms

from .models import Files, Images, PDF


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file', )


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('file', )


class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ('file', )
