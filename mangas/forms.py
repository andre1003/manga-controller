from django import forms

from mangas.models import Manga


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'chapter', 'url', 'notes', 'status', 'image']
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
                    'placeholder': "Chapter"
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

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
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
        fields = ['title', 'chapter', 'url', 'status', 'notes']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'chapter': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert additional info, links, etc.',
                    'rows': '3'
                }
            ),
        }
