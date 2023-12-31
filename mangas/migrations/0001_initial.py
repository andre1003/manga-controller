# Generated by Django 4.2.1 on 2023-07-15 20:34

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
            name='Manga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('chapter', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='manga-imgs/')),
                ('url', models.URLField(blank=True, default=None, help_text='Works better with Mangalivre website.', null=True)),
                ('status', models.IntegerField(choices=[(0, 'Ongoing'), (1, 'Finished'), (2, 'Wish to read'), (3, 'Dropped')], default=0)),
                ('notes', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
