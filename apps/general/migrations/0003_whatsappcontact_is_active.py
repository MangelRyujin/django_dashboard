# Generated by Django 5.0.6 on 2024-09-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_localsales_shopsales'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsappcontact',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
