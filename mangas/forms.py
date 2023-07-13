from django import forms

from mangas.models import Manga


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'chapter', 'url', 'notes', 'image']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Manga title'
                }
            ),

            'chapter': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Chapter you stopped"
                }
            ),

            'url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Manga URL'
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert additional info, links, etc.'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class MangaUpdateForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'chapter', 'url', 'is_finished', 'notes']

        widgets = {
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert additional info, links, etc.',
                    'rows': '3'
                }
            ),
        }
