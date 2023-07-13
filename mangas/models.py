from uuid import uuid4

from django.db import models
from users.models import User


class Manga(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    title = models.CharField(max_length=40)
    chapter = models.IntegerField()
    image = models.ImageField(upload_to='manga-imgs/', blank=True, null=True)

    url = models.URLField(max_length=200, default=None, blank=True, null=True)

    is_finished = models.BooleanField(default=False)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title