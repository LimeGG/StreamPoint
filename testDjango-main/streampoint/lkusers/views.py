import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shop.models import AddProduct
from streamers.models import AllStreamers
from .forms import *
from .models import *
import json


settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
print(settings_module)


def show_profile(request):
    user_id = request.user.id
    user = ContribUsers.objects.get(id=user_id)
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if not request.user.groups.filter(name='Streamer'):
            streamers = HisStreamers.objects.filter(user_id=user_id)
            name1 = User.objects.filter(id=user_id)
            name = name1[0]
            form = addPhoto_Telega(request.POST, request.FILES, instance=user)

            if form.is_valid():
                try:
                    form.save()
                    return redirect('Profile')
                except:
                    form.add_error(None, "Ошибка добавления данных")
            return render(request, "profile/profile.html", {"streamers": streamers, "name": name, "form": form})
        else:

            stream_name = AllStreamers.objects.get(streamer=user_id)
            id_stream = stream_name.pk
            buy = UserBuy.objects.filter(streamer_id=id_stream)
            user_id = request.user.id
            stream = AllStreamers.objects.filter(streamer=user_id)
            name = User.objects.get(id=user_id)
            return render(request, "profile/profilestreamer.html", {"streamer": stream, "name": name, "buy": buy})


def show_shopstreamer(request):
    user_id = request.user.id
    stream_name = AllStreamers.objects.get(streamer=user_id)
    id_stream = stream_name.pk
    product = AddProduct.objects.filter(streamer_id=id_stream, published=1)
    return render(request, "profile/streamersshop.html",
                  {"stream_name": stream_name, "product": product})





def addproduct(request):
    user_id = request.user.id
    stream_name = AllStreamers.objects.get(streamer=user_id)
    id_stream = stream_name.pk
    if request.method == "POST":
        form = AddproductForms(request.POST, request.FILES)
        if form.is_valid():
            addproduct = form.save(commit=False)
            addproduct.streamer_id = id_stream
            try:
                form.save()
                return redirect("myshopp")
            except:
                form.add_error(None, "Ошибка добавления товара")
    else:
        form = AddproductForms()
    return render(request, "profile/addproduct.html", {"form": form})


def deleteproduct(request, pk):
    print(type(pk))
    if request.method == "POST":
        product = AddProduct.objects.get(id=pk)
        form = DeleteProductforms(request.POST, instance=product)
        print(type(pk))
        if form.is_valid():
            delete = form.save(commit=False)
            delete.published = 0
            try:
                form.save()
                return redirect("myshopp")
            except:
                form.add_error(None, "Ошибка удаления товара")
    else:
        form = DeleteProductforms()
    return render(request, "profile/deleteproduct.html", {"form": form})


def MyView(request):
    user_id = request.user.id
    data = {"user_id": user_id}
    json_data = json.dumps(data)
    response = HttpResponse(json_data, content_type='application/json')
    response.set_cookie('user_id', user_id)
    print(user_id)
    return response








