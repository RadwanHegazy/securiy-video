from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('WatchVideo/<str:uuid>', views.watch_video,name='wv'),

    # authentication
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

]