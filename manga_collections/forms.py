from django import forms

from manga_collections.models import MangaCollection


class MangaCollectionCreationForm(forms.ModelForm):
    class Meta:
        model = MangaCollection
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Manga title'
                }
            ),

            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class MangaCollectionUpdateForm(forms.ModelForm):
    want = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = MangaCollection
        fields = ['title', 'status', 'bought']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def save(self, commit=True):
        return super(MangaCollectionUpdateForm, self).save(commit=commit)
    