# Generated by Django 4.1 on 2023-02-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lkusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hisstreamers',
            name='photouser',
            field=models.ImageField(blank=True, null=True, upload_to='photousers/', verbose_name='Фото пользователя'),
        ),
    ]