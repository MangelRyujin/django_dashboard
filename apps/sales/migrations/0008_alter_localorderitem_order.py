# Generated by Django 5.0.6 on 2024-09-30 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_alter_localorderitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localorderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.localorder', verbose_name='local_order_item'),
        ),
    ]
