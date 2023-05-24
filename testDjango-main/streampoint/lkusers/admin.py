from django.contrib import admin
from .models import ContribUsers, HisStreamers, UserBuy, Achievements, Allachievements

admin.site.register(ContribUsers)
admin.site.register(Achievements)


@admin.register(HisStreamers)
class HisStreamersAdmin(admin.ModelAdmin):
    list_display = ("user", "points", "streamers")
    list_filter = ("user_id",)


@admin.register(UserBuy)
class UserBuyAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "streamer")
    list_filter = ("user",)


# @admin.register(Achievements)
# class AchievementsAdmin(admin.ModelAdmin):
#     list_display = ("achievement", "user")
#     list_filter = ("user",)

@admin.register(Allachievements)
class AllachievementsAdmin(admin.ModelAdmin):
    list_display = ("name", "reward", "conditions")
    list_filter = ("name",)
