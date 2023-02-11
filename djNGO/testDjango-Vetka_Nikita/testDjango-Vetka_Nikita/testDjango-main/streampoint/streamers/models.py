from django.db import models


class AllStreamers(models.Model):
    name = models.CharField("Имя стримера", max_length=200)
    photo = models.ImageField("Фото", upload_to="photostream/")
    urltwitch = models.URLField("Ссылка на твич", max_length=200)

    class Meta:
        verbose_name = "Все стримеры"
        verbose_name_plural = "Все стримеры"

    def __str__(self):
        return self.name
