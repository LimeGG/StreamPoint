from django.db import models

from lkusers.models import ContribUsers
from shop.models import AddProduct

class AllStreamers(models.Model):
    name = models.CharField("Имя стримера", max_length=200)
    photo = models.ImageField("Фото", upload_to="photostream/")
    urltwitch = models.URLField("Ссылка на твич", max_length=200)
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(ContribUsers, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Все стримеры"
        verbose_name_plural = "Все стримеры"
