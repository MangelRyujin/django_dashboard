# Generated by Django 5.0.6 on 2024-10-05 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_remove_localorderitemstock_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cash'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transfer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Transfer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_ci',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User ci'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User full name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User id'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User phone'),
        ),
    ]
