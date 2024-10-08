# Generated by Django 5.0.6 on 2024-07-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_image_historicalproduct_image_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='image_three',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='image_two',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_three',
            field=models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Image'),
        ),
    ]
