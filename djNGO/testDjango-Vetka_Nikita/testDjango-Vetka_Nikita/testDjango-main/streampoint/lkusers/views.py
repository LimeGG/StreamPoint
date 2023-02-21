from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import UserProfileForm

def show_profile(request):
    user_id = request.user.id
    form = UserProfileForm
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        streamers = HisStreamers.objects.filter(user_id=user_id)
        name1 = User.objects.filter(id=user_id)
        name = name1[0]
        return render(request, "profile/profile.html", { "streamers": streamers, "name": name, 'form': form})




