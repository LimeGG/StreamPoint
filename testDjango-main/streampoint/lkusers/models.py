from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from streamers.models import AllStreamers
from shop.models import AddProduct


class ContribUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photouser = models.ImageField("Фото пользователя", upload_to="photousers/", null=True, blank=True)
    telegramm = models.CharField("телегарм", max_length=200, help_text="Телеграм пользователя")
<<<<<<< Updated upstream
    ref = models.IntegerField("Рефералы", blank=True, null=True)
=======
    referral_name = models.CharField(max_length=50, blank=True, null=True)
>>>>>>> Stashed changes

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.user)


class Allachievements(models.Model):
    name = models.CharField("Имя", max_length=200)
    imagelogo = models.ImageField("Фото достижения", upload_to="photooachivment/", null=True, blank=True)
    reward = models.IntegerField("Баллы за достижение", default=0)
    conditions = models.CharField("условие получения достижения", max_length=200)

    class Meta:
        verbose_name = "Все достижения"
        verbose_name_plural = "Все достижения"

    def __str__(self):
        return str(self.name)


class Achievements(models.Model):
    achievement = models.ForeignKey(Allachievements, on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "достижения пользователя"
        verbose_name_plural = "достижения пользователя"

    # def __str__(self):
    #     return str(self.achievement)


class HisStreamers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    points = models.IntegerField("Очки за блогера", blank=True, null=True, default=0)
    streamers = models.ForeignKey(AllStreamers, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = "Стримеры пользователя"
        verbose_name_plural = "Стримеры пользователей"

    def __str__(self):
        return str(self.streamers)

    def get_absolute_url(self):
        return reverse('streamer', kwargs={'user': self.pk})


class UserBuy(models.Model):
    user = models.ForeignKey("ContribUsers", on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE, blank=True,
                                null=True)  # on_delete=models.DO_NOTHING
    streamer = models.ForeignKey(AllStreamers, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Товар пользователя"
        verbose_name_plural = "Товары Пользователей"


@receiver(post_save, sender=User)
def created_user_profile(sender, instance, created, **kwargs):
    # streamers = AllStreamers.objects.all()
    if created:
        ContribUsers.objects.create(user=instance)
    # for streamer in streamers:
    #     try:
    #         if created:
    #             HisStreamers.objects.create(user=instance, streamers_id=streamer.id)
    #     except:
    #         break


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.ContribUsers.save()
    # instance.HisStreamers.save()
