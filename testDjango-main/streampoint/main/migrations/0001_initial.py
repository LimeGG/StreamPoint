# Generated by Django 4.1 on 2023-01-26 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllStreamers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('photo', models.ImageField(upload_to='strim_image/', verbose_name='Фото стримера')),
                ('url_twitch', models.URLField(verbose_name='Ссылка на twitch')),
                ('shop', models.BooleanField(default=False, verbose_name='Наличие магазина')),
            ],
            options={
                'verbose_name': 'Все стримеры',
                'verbose_name_plural': 'Все стримеры',
            },
        ),
        migrations.CreateModel(
            name='HisStreamers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(null=True, verbose_name='Очки стримеров')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Name_strimers', to='main.allstreamers', verbose_name='Имя')),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Photo_strimers', to='main.allstreamers', verbose_name='Фото стримера')),
                ('url_twitch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Url_strimers', to='main.allstreamers', verbose_name='Ссылка на twitch')),
            ],
            options={
                'verbose_name': 'Стримеры пользователя',
                'verbose_name_plural': 'Стримеры пользователя',
            },
        ),
        migrations.CreateModel(
            name='ShopStreamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(null=True, verbose_name='Цена товара')),
                ('title', models.CharField(max_length=200, verbose_name='Название товара')),
                ('photo', models.ImageField(upload_to='shop_image/', verbose_name='Фото товара')),
            ],
            options={
                'verbose_name': 'Магазин Стримера',
                'verbose_name_plural': 'Магазины стримеров',
            },
        ),
        migrations.CreateModel(
            name='UsersBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('login', models.EmailField(max_length=200, verbose_name='Почта')),
                ('password', models.TextField(max_length=200, verbose_name='Пароль')),
                ('photo', models.ImageField(upload_to='user_image/', verbose_name='Фото профиля')),
                ('points', models.ManyToManyField(related_name='His_streamers', to='main.hisstreamers', verbose_name='Стримеры')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]