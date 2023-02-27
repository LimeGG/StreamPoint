from django.conf import settings
from django.shortcuts import render, redirect
from .models import *
from streamers.models import AllStreamers
from django.contrib.auth.models import User
from shop.models import AddProduct
from .forms import *
from django.views.generic import DeleteView

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
    user_id = request.user.id
    # stream_name = AllStreamers.objects.get(streamer=user_id)
    # id_stream = stream_name.pk
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
                form.add_error(None, "Ошибка добавления товара")
    else:
        form = DeleteProductforms()
    return render(request, "profile/deleteproduct.html", {"form": form})



# class DeleteProduct(DeleteView):
#     model = AddProduct
#     template_name = "profile/deleteproduct.html"
#     success_url = "/lkusers/myshop"
