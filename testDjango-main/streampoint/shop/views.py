from django.shortcuts import render
from .models import *


def index(request):
    product = AddProduct.objects.all()
    return render(request, 'shop/shop.html', {"product": product})
