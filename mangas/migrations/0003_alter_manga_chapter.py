# Generated by Django 4.2.1 on 2023-07-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0002_rename_user_manga_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='chapter',
            field=models.IntegerField(),
        ),
    ]
