from django.db import models


class AllStreamers(models.Model):
    name = models.CharField("Имя", max_length=100)
    photo = models.ImageField("Фото стримера", upload_to="strim_image/")
    url_twitch = models.URLField("Ссылка на twitch", max_length=200)
    shop = models.BooleanField("Наличие магазина", default=False)

    class Meta:
        verbose_name = "Все стримеры"
        verbose_name_plural = "Все стримеры"




class HisStreamers(models.Model):
    name = models.OneToOneField(AllStreamers, verbose_name="Имя", related_name="Name_strimers",
                                on_delete=models.CASCADE)
    photo = models.OneToOneField(AllStreamers, verbose_name="Фото стримера", related_name="Photo_strimers",
                                 on_delete=models.CASCADE)
    url_twitch = models.OneToOneField(AllStreamers, verbose_name="Ссылка на twitch", related_name="Url_strimers",
                                      on_delete=models.CASCADE)
    points = models.IntegerField("Очки стримеров", null=True)

    class Meta:
        verbose_name = "Стримеры пользователя"
        verbose_name_plural = "Стримеры пользователя"


class UsersBase(models.Model):
    name = models.CharField("Имя", max_length=100)
    login = models.EmailField("Почта", max_length=200)
    password = models.TextField("Пароль", max_length=200)
    photo = models.ImageField("Фото профиля", upload_to="user_image/")
    points = models.ManyToManyField(HisStreamers, verbose_name="Стримеры", related_name="His_streamers")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class ShopStreamer(models.Model):
    price = models.IntegerField("Цена товара", null=True)
    title = models.CharField("Название товара", max_length=200)
    photo = models.ImageField("Фото товара", upload_to="shop_image/")

    class Meta:
        verbose_name = "Магазин Стримера"
        verbose_name_plural = "Магазины стримеров"
