# Generated by Django 5.0.6 on 2024-07-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_historicalproduct_image_remove_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='image',
            field=models.TextField(default=1, max_length=100, verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='product_images', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='HistoricalProductImage',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
