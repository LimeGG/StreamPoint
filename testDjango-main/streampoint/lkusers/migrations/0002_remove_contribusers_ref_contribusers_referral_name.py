# Generated by Django 4.2.1 on 2023-06-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lkusers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribusers',
            name='ref',
        ),
        migrations.AddField(
            model_name='contribusers',
            name='referral_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
