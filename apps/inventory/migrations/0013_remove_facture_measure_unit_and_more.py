# Generated by Django 5.0.6 on 2024-10-09 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_stockmovements_cant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='measure_unit',
        ),
        migrations.AlterField(
            model_name='facture',
            name='cant',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cant'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cant',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cant'),
        ),
        migrations.AlterField(
            model_name='stockmovements',
            name='cant',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cant'),
        ),
    ]
