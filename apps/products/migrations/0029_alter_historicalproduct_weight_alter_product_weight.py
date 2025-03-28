# Generated by Django 5.0.6 on 2024-12-27 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_alter_offert_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='weight',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price'),
        ),
    ]
