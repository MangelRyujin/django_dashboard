# Generated by Django 5.0.6 on 2024-09-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_whatsappcontact_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='image',
            field=models.ImageField(default=1, upload_to='logo_site', verbose_name='Logo'),
            preserve_default=False,
        ),
    ]