# Generated by Django 5.0.6 on 2024-11-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0015_shoporderitemstock'),
    ]

    operations = [
        migrations.AddField(
            model_name='localorderitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Discount'),
        ),
    ]
