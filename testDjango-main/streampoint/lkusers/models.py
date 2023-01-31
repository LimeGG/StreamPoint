from django.db import models

from django.contrib.auth.models import User


class ContribUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователи"


class HisStreamers(models.Model):
    user = models.ForeignKey(ContribUsers, on_delete=models.CASCADE)
    points = models.IntegerField("Очки за блогера", blank=True)
    urltwitch = models.URLField("Ссылка на стримера", max_length= 200, )

    class Meta:
        verbose_name = "Стримеры пользователя"
