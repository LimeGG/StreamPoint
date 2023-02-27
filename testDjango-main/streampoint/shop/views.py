from django.contrib import messages
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
    streamer = AllStreamers.objects.get(id=streamer_id)
    try:
        points1 = HisStreamers.objects.filter(streamers_id=streamer_id, user_id=user_id)
        points = points1[0]
    except:
        points = 0
    product = AddProduct.objects.filter(streamer_id=streamer_id)

    return render(request, "shop/shop.html",
                  {"product": product, "streamer": streamer, "points": points})


def buyproduct(request, pk):
    """
    здесь добавляется товар в корзину и проверятеся хватает ли баллов на покупку
    """
    user_id = request.user.id
    if request.method == "POST":
        streamer = AddProduct.objects.filter(id=pk)
        streamer_ = streamer[0]
        streamer_id = streamer_.streamer_id
        user = HisStreamers.objects.get(user_id=user_id, streamers_id=streamer_id)
        form = BuyproductForms(request.POST, request.FILES)
        form_balance = BalanceCheckForms(request.POST, instance=user)
        if form.is_valid() and form_balance.is_valid():
            checkbalance = form_balance.save(commit=False)
            buyproduct1 = form.save(commit=False)
            price1 = AddProduct.objects.filter(id=pk)
            price_ = price1[0]
            price = price_.price
            buyproduct1.user_id = user_id
            print(streamer_id)
            buyproduct1.product_id = pk
            buyproduct1.streamer_id = streamer_id
            points1 = HisStreamers.objects.filter(streamers_id=streamer_id, user_id=user_id)
            points_ = points1[0]
            point = points_.points
            if point >= price:
                i = point - price
                checkbalance.points = i
                form.save()
                form_balance.save()
                messages.success(request, 'Товар успешно куплен')
                return redirect("Shopstreamer", streamer_id)
            else:
                return redirect("Shop")
    else:
        form = BuyproductForms()
        form_balance = BalanceCheckForms()
    return render(request, "shop/byproduct.html", {"form": form, "form1": form_balance})
