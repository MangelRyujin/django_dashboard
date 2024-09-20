# Generated by Django 5.0.6 on 2024-09-15 08:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_stock_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='measure_unit',
            field=models.CharField(choices=[('m', 'milliliters'), ('g', 'grams'), ('u', 'units')], default='u', max_length=1, verbose_name='Measure unit'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cant',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cant'),
        ),
    ]