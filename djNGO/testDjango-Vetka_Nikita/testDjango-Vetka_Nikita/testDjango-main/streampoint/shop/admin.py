from django.contrib import admin
from .models import AddProduct


@admin.register(AddProduct)
class AddProduct(admin.ModelAdmin):
    list_display = ("nameproduct", "price", "streamer")
    list_filter = ("streamer",)