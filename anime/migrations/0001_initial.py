# Generated by Django 4.2.1 on 2023-07-16 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('episode', models.IntegerField(default=1)),
                ('status', models.IntegerField(choices=[(0, 'Watching'), (1, 'Finished'), (2, 'Wish'), (3, 'Stopped')], default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='anime-imgs/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
