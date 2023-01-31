from django.db import models


class ShopStreamers(models.Model):
    namestreamers = models.CharField("Имя стримера", max_length=200, help_text="Введите имя блогера")
    name = models.CharField("Товар", max_length=200, help_text="Наименование товара")
    price = models.IntegerField("цена товара")
    photoproduct = models.ImageField("Фото товара", upload_to="photoproduct/", help_text="фото товара")
    photostreamers = models.ImageField("Фото блогера", upload_to="photostreamers/",help_text="Фото стримера")

    class Meta:
        verbose_name = "Магазин стримера"