# Generated by Django 4.2.1 on 2023-05-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lkusers', '0002_rename_referal_contribusers_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribusers',
            name='ref',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рефералы'),
        ),
    ]
