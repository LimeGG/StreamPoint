from django.shortcuts import render

def stream(request):
    #point = HisStreamers.objects.all()
    return render(request, 'streamers/streamers.html')