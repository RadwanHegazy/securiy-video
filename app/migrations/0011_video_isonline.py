# Generated by Django 4.2.2 on 2023-06-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_video_isdone'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='isOnline',
            field=models.BooleanField(default=True),
        ),
    ]
