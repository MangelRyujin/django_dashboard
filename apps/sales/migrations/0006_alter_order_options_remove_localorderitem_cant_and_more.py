# Generated by Django 5.0.6 on 2024-09-30 23:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_supplier_email_alter_supplier_image'),
        ('sales', '0005_localorder_localorderitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Orden', 'verbose_name_plural': 'Orders'},
        ),
        migrations.RemoveField(
            model_name='localorderitem',
            name='cant',
        ),
        migrations.RemoveField(
            model_name='localorderitem',
            name='total_cost',
        ),
        migrations.RemoveField(
            model_name='localorderitem',
            name='total_price',
        ),
        migrations.AddField(
            model_name='localorder',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='localorder',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='localorder',
            name='user_ci',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User ci'),
        ),
        migrations.AddField(
            model_name='localorder',
            name='user_full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User full name'),
        ),
        migrations.AddField(
            model_name='localorder',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User id'),
        ),
        migrations.AddField(
            model_name='localorder',
            name='user_phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='User phone'),
        ),
        migrations.CreateModel(
            name='LocalOrderItemStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant', models.PositiveIntegerField(verbose_name='Cant')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.localorderitem', verbose_name='local_order_item_stock')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.stock', verbose_name='local_stock_item')),
            ],
            options={
                'verbose_name': 'Local order',
                'verbose_name_plural': 'Local orders',
            },
        ),
    ]