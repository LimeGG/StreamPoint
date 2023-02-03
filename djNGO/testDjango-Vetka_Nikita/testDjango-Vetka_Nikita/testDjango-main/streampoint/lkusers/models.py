from django.db import models

from django.contrib.auth.models import User


class ContribUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photouser = models.ImageField("Фото пользователя", upload_to="photousers/", null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"




class HisStreamers(models.Model):
    user = models.ForeignKey(ContribUsers, on_delete=models.CASCADE)
    points = models.IntegerField("Очки за блогера", blank=True, null=True)
    urltwitch = models.URLField("Ссылка на стримера", max_length=200)

    class Meta:
        verbose_name = "Стримеры пользователя"
        verbose_name_plural = "Стримеры пользователей"

    def __str__(self):
        return f"ссылка на твич: {self.urltwitch}"
