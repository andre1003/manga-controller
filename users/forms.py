from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from users.models import User


# User creation form
class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['email']
        field_classes = {'email': forms.EmailField}


# User change form
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = User
        fields = "__all__"
        field_classes = {'email': forms.EmailField}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format(
                f"../../{self.instance.pk}/password/"
            )