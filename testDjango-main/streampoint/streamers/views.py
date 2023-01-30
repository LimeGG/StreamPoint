from django.shortcuts import render
from .models import HisStreamers
def stream(request):
    point = HisStreamers.objects.all()
    return render (request, 'streamers/streamers.html', {'point': point})