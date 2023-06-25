# Generated by Django 4.2.2 on 2023-06-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_video_audio_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_uuid',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='durations',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/video-2023-06-19'),
        ),
    ]