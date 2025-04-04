# Generated by Django 5.0.6 on 2024-09-30 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_historicaluser_ci_alter_user_ci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, verbose_name='dirección de correo electrónico'),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='dirección de correo electrónico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users_images', verbose_name='Imagen'),
        ),
    ]
