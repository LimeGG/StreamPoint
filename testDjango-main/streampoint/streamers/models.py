from django.db import models


class AllStreamers(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото стримера", upload_to="strim_image/")
    url_twitch = models.URLField("Ссылка на twitch", max_length=200)
    shop = models.BooleanField("Наличие магазина", default=False)





class HisStreamers(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото стримера", upload_to="strim_image/")
    url_twitch = models.URLField("Ссылка на twitch", max_length=200)
    points = models.IntegerField("Очки стримеров", null=True)


