# Generated by Django 4.0 on 2023-06-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_multiplay'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
