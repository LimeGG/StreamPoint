from django.contrib import admin
from .models import ContribUsers, HisStreamers, UserBuy

admin.site.register(ContribUsers)


@admin.register(HisStreamers)
class HisStreamersAdmin(admin.ModelAdmin):
    list_display = ("user", "points", "streamers")
    list_filter = ("user_id",)


@admin.register(UserBuy)
class UserBuyAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "streamer")
    list_filter = ("user",)
