from django import forms

from anime.models import Anime


class AnimeCreationForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'episode', 'status', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert anime title'
                }
            ),

            'episode': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert anime episode'
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


class AnimeUpdateForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'episode', 'status']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert anime title'
                }
            ),

            'episode': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insert anime episode'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }
