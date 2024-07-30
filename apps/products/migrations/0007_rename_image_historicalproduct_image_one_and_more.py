# Generated by Django 5.0.6 on 2024-07-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_historicalproduct_code_product_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalproduct',
            old_name='image',
            new_name='image_one',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_one',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='image_three',
            field=models.TextField(default=1, max_length=100, verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='image_two',
            field=models.TextField(default=1, max_length=100, verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_three',
            field=models.ImageField(default=1, upload_to='product_images', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_two',
            field=models.ImageField(default=1, upload_to='product_images', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
