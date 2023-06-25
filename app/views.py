from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import auth_login
from django.contrib.auth import authenticate

def watch_video (request,uuid) :

    video = Video.objects.get(video_uuid = uuid)

    if video.isDone == False :
        return HttpResponse('جاري العمل علي الفيديو..')

    if video.isOnline == False :
        return render(request,'offline.html')

    duration = video.durations
    
    audio = f'/media/audio/{uuid}.mp3'



    return render(request,'watchVideo.html',{'VideoName':video.name,'durations':duration,'audio':audio,"uuid":uuid})



@csrf_exempt
@login_required
def profile (request) :
    
    context = {}

    user = request.user
    videos = Video.objects.filter(user = user).order_by('date')

    if request.method == "POST" :
        video = request.FILES['video']
        name = str(video.name)
        video.name = 'video.mp4'

        Video.objects.create(user = user, video = video, name = name)

        return redirect('profile')

    if 'delete' in request.GET :
        delete = request.GET['delete']
        Video.objects.get(id=delete).delete()
        return redirect('profile')

    if 'status' in request.GET :
        status = request.GET['status']
        video_id = request.GET['id']
        v = Video.objects.get( id = video_id)
        v.isOnline = status
        v.save()
        return redirect('profile')
    

    context['videos'] = videos
    
    return render(request,'profile.html',context)



def register (request) :

    if request.method == "POST" :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create(
            username = username,
            email = email,
        )

        user.set_password(password)
        user.save()

        auth_login(request,user=user)
        return redirect('profile')


    return render(request,'register.html')

def login (request) :

    if request.method == "POST" :

        email = request.POST['email']
        password = request.POST['password']

        getUser = User.objects.get(email = email)
        auth = authenticate(username = getUser.username ,password = password)
        
        if auth != None :
            auth_login(request,user=getUser)
            return redirect('profile')

    return render(request,'login.html')


def index (request) :

    if request.user.is_authenticated :
        return redirect('profile')
    
    return render(request,'index.html')