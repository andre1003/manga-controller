from __future__ import unicode_literals

from uuid import uuid4

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from users.managers import UserManager


# Override AbstractBaseUser to fit this project
class User(AbstractBaseUser, PermissionsMixin):
    # ID
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # Personal info
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Controllers
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    # Objects
    objects = UserManager()

    # Use e-mail instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    # Define meta class
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    # Get user full name
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    # Get user short name
    def get_short_name(self):
        return self.first_name
    
    # Send email to this user
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)