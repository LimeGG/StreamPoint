from django.db import models
from streamers.models import AllStreamers


class ShopStreamers(models.Model):
    namestreamers = models.OneToOneField(AllStreamers, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Магазин стримера"
        verbose_name_plural = "МАгазин стримера"


class AddProduct(models.Model):
    nameproduct = models.CharField("Наименование товара", max_length=200)
    photoproduct = models.ImageField("Фото товара", upload_to="photoproduct/", help_text="фото товара")
    price = models.IntegerField("цена товара")
    shop = models.ForeignKey(ShopStreamers, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
