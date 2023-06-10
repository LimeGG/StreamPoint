from django.http import HttpResponse
from django.shortcuts import render
from streamers.models import AllStreamers
from lkusers.models import HisStreamers
from django.db.models import Count

def stream(request):

    jpg = AllStreamers.objects.all()
    his_streamers1 = HisStreamers.objects.all()
    his_streamers2 = his_streamers1.annotate(user_count=Count('user'))
    his_streamers3 = his_streamers2.order_by('-user_count')
    his_streamers = his_streamers3[:5]
    return render(request, 'main/index.html', {'jpg': jpg, "hs": his_streamers})