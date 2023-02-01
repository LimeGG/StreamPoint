<<<<<<< Updated upstream
# Generated by Django 4.1 on 2023-01-31 20:47
=======
# Generated by Django 4.1 on 2023-02-01 08:06
>>>>>>> Stashed changes

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
                ('name', models.CharField(max_length=200, verbose_name='Имя стримера')),
                ('photo', models.ImageField(upload_to='photostream/', verbose_name='Фото')),
                ('urltwitch', models.URLField(verbose_name='Ссылка на твич')),
                ('shop', models.BooleanField(default=False, verbose_name='Наличие магазина')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lkusers.contribusers')),
            ],
            options={
                'verbose_name': 'Все стримеры',
<<<<<<< Updated upstream
=======
                'verbose_name_plural': 'Все стримеры',
>>>>>>> Stashed changes
            },
        ),
    ]
