# Generated by Django 4.2.1 on 2023-07-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0005_manga_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
