from django.contrib import admin
from .models import Video#, Multiplay
from django.contrib.auth.models import Group

# admin.site.register(Multiplay)
admin.site.register(Video)

admin.site.unregister(Group)