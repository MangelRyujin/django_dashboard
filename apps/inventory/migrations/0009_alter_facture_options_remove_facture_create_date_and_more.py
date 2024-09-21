# Generated by Django 5.0.6 on 2024-09-21 00:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_remove_supplier_name_supplier_ci_supplier_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facture',
            options={'verbose_name': 'Facture', 'verbose_name_plural': 'Factures'},
        ),
        migrations.RemoveField(
            model_name='facture',
            name='create_date',
        ),
        migrations.AddField(
            model_name='facture',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
    ]
