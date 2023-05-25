from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class AllStreamers(models.Model):
    streamer = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Имя стримера", max_length=200)
    photo = models.ImageField("Фото", upload_to="photostream/", blank=True, null=True)
    urltwitch = models.URLField("Ссылка на твич", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Все стримеры"
        verbose_name_plural = "Все стримеры"
        permissions = [
            ("shop.add_AddProduct", "add product"),
            ("shop.change_AddProduct", "change product"),
            ("shop.delete_AddProduct", "delete product"),
            ("shop.view_AddProduct", "view product"),
        ]

    def __str__(self):
        return str(self.streamer)

    def get_absolute_url(self):
        return reverse('streamer', kwargs={'streamer_id': self.pk})



