from django.db import models
from django.urls import reverse
from streamers.models import AllStreamers


class AddProduct(models.Model):
    nameproduct = models.CharField("Наименование товара", max_length=200)
    photoproduct = models.ImageField("Фото товара", upload_to="photoproduct/", help_text="фото товара")
    price = models.IntegerField("цена товара")
    streamer = models.ForeignKey(AllStreamers, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.nameproduct

    def get_absolute_url(self):
        return reverse('shop', kwargs={'streamer_id': self.pk})
