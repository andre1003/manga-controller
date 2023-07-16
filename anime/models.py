from uuid import uuid4

from django.db import models
from django.conf import settings


class Anime(models.Model):
    STATUS_CHOICE = (
        (0, 'Watching'),
        (1, 'Finished'),
        (2, 'Wish'),
        (3, 'Stopped')
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    title = models.CharField(max_length=40)
    episode = models.IntegerField(default=1)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    image = models.ImageField(upload_to='anime-imgs/', blank=True, null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
