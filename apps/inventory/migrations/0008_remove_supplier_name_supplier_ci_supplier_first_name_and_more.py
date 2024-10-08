# Generated by Django 5.0.6 on 2024-09-20 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_stockmovements_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='name',
        ),
        migrations.AddField(
            model_name='supplier',
            name='ci',
            field=models.CharField(default=1, max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='first_name',
            field=models.CharField(default=1, max_length=100, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplier',
            name='last_name',
            field=models.CharField(default=1, max_length=100, verbose_name='Last name'),
            preserve_default=False,
        ),
    ]
