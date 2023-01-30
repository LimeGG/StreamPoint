from django.db import models

from django.contrib.auth.models import User

"""
Таблица с пользователями, связывается с таблицей джанго пользователей, также связвается с таблицей стримеров, 
которых смотрит пользователь
"""


class ContribUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    streamers = models.ForeignKey("Hisstreamers", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователи"

    def __str__(self):
        return self.user


class Hisstreamers(models.Model):
    name = models.CharField("Имя", max_length=200)
    photo = models.ImageField("Фото", upload_to="streamers_photo/")
    points = models.IntegerField("Очки за блогера", blank=True)

    class Meta:
        verbose_name = "Стримеры пользователя"

    def __str__(self):
        return self.name
