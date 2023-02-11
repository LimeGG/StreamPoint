from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from .models import *

def show_profile(request):
    user_id = request.user.id
    streamers = HisStreamers.objects.filter(user_id=user_id)
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        streamers = HisStreamers.object.filter(user_id=user_id)
        name1 = User.object.filter(id=user_id)
        name = name1[0]
        return render(request, 'profile/profile.html',{"streamers": streamers, "name": name})
