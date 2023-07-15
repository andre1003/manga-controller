from uuid import uuid4

from django.db import models
from users.models import User

import simplejson as json


class MangaCollection(models.Model):
    STATUS_CHOICE = (
        (0, 'Buying'),
        (1, 'Finished'),
        (2, 'Wish')
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    title = models.CharField(max_length=40)
    bought = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='manga-collection-imgs/', blank=True, null=True)

    status = models.IntegerField(choices=STATUS_CHOICE, default=0)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_bought_list(self):
        json_dec = json.decoder.JSONDecoder()
        return json_dec.decode(self.bought)
    
    def get_bought_str(self):
        if not self.bought or self.bought == '[]':
            return 'No volumes bought yet!'
        
        json_dec = json.decoder.JSONDecoder()
        volumes = json_dec.decode(self.bought)
        text = ''
        volumes = [int(volume) for volume in volumes]
        volumes.sort()

        for volume in volumes:
            text += str(volume) + ', '
        text = text.removesuffix(', ')
        return text
    