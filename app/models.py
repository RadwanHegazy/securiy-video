from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import uuid
import cv2
import numpy as np




class Video (models.Model) :
    name = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    video_uuid = models.TextField(default='',blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_video')
    video = models.FileField(upload_to='videos')
    durations = models.TextField(default='',blank=True,null=True)
    isDone = models.BooleanField(default=False)
    isOnline = models.BooleanField(default=True)

    def __str__(self) :
        return f'{self.name}'




def save_ (video) :

    durations = images.main(video_file = os.getcwd() + video.video.url , uuid = video.video_uuid)
    video.durations = durations

    video.isDone = True
    video.save()



from . import images
import os
import threading

@receiver(post_save,sender=Video)
def work_on_video (**response) :
    
    
    if response['created'] :

        myuuid = uuid.uuid4()
        video = response['instance']
        
        video.video_uuid = myuuid
        video.save()

        threading.Thread(target=save_,args=(video,)).start()
