from django.shortcuts import render
from .models import AllStreamers

def stream(request):
    jpg = AllStreamers.objects.all()
    return render(request, 'streamers/streamers.html', {'jpg': jpg})