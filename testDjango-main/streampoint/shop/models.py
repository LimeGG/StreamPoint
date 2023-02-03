from django.db import models
# from streamers.models import AllStreamers





class AddProduct(models.Model):
    nameproduct = models.CharField("Наименование товара", max_length=200)
    photoproduct = models.ImageField("Фото товара", upload_to="photoproduct/", help_text="фото товара")
    price = models.IntegerField("цена товара")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
