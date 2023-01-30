# Generated by Django 4.1 on 2023-01-30 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lkusers', '0001_initial'),
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
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lkusers.contribusers')),
            ],
            options={
                'verbose_name': 'Все стримеры',
                'verbose_name_plural': 'Все стримеры',
            },
        ),
    ]