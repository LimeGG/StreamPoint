from django.contrib import admin
from .models import AllStreamers



@admin.register(AllStreamers)
class AllStreamersAdmin(admin.ModelAdmin):
    list_display = ("name", "urltwitch")