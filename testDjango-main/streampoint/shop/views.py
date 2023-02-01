from django.shortcuts import render
from .models import *


def index(request):
    product = AddProduct.objects.all()
    photostreamers = ShopStreamers.objects.all()
    return render(request, 'shop/shop.html', {"product": product, "photostreamers": photostreamers})
