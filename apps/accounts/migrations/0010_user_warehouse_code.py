# Generated by Django 5.0.6 on 2025-01-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_delete_historicaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='warehouse_code',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Warehouse'),
        ),
    ]
