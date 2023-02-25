from django.shortcuts import render, redirect
from .models import *
from streamers.models import AllStreamers
from lkusers.models import HisStreamers
from .forms import *


def stream(request):
    jpg = AllStreamers.objects.all()
    return render(request, 'shop/streamers.html', {'jpg': jpg})


def show_shop(request, streamer_id):
    user_id = request.user.id
    points1 = HisStreamers.objects.filter(streamers_id=streamer_id, user_id=user_id)
    product = AddProduct.objects.filter(streamer_id=streamer_id)
    name = product[0]
    points = points1[0]
    print(points)
    return render(request, "shop/shop.html",
                  {"product": product, "streamer": streamer_id, "name": name, "points": points})


def buyproduct(request, pk):
    user_id = request.user.id
    if request.method == "POST":
        form = BuyproductForms(request.POST, request.FILES)
        if form.is_valid():
            buyproduct1 = form.save(commit=False)
            buyproduct1.user_id = user_id
            streamer = AddProduct.objects.filter(id=pk)
            streamer_ = streamer[0]
            streamer_id = streamer_.streamer_id
            buyproduct1.product_id = pk
            buyproduct1.streamer_id = streamer_id
            form.save()
            return redirect("Shop")
    else:
        form = BuyproductForms()

    return render(request, "shop/byproduct.html", {"form": form})

