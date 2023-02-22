from django.conf import settings
from django.shortcuts import render, redirect
from .models import *
from streamers.models import AllStreamers
from django.contrib.auth.models import User


def show_profile(request):
    user_id = request.user.id
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if not request.user.groups.filter(name='Streamer'):
            streamers = HisStreamers.objects.filter(user_id=user_id)
            name1 = User.objects.filter(id=user_id)
            name = name1[0]
            return render(request, "profile/profile.html", {"streamers": streamers, "name": name})
        else:
            stream = AllStreamers.objects.filter(streamer=user_id)
            name1 = User.objects.filter(id=user_id)
            name = name1[0]
            return render(request, "profile/profilestreamer.html", {"streamer": stream, "namm": name})
