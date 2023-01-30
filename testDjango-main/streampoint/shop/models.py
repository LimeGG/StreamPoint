from django.db import models

class ShopStreamer(models.Model):
    price = models.IntegerField("Цена товара", null=True)
    title = models.CharField("Название товара", max_length=200)
    photo = models.ImageField("Фото товара", upload_to="shop_image/")

    class Meta:
        verbose_name = "Магазин Стримера"
        verbose_name_plural = "Магазины стримеров"

