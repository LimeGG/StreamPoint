from django.db import models
from lkusers.models import ContribUsers

"""
Это таблица со всеми стримерами, связывается с таблицей пользователей
"""


class AllStreamers(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото стримера", upload_to="strim_image/")
    url_twitch = models.URLField("Ссылка на twitch", max_length=200)
    shop = models.BooleanField("Наличие магазина", default=False)
    user = models.ForeignKey(ContribUsers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Все стримеры"
        verbose_name_plural = "Все стримеры"

    def __str__(self):
        return self.name
