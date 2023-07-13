from django import forms

from mangas.models import Manga


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'chapter', 'url', 'image']


class MangaUpdateForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'chapter', 'url', 'is_finished']
        