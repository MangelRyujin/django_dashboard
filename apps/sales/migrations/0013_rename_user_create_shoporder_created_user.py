# Generated by Django 5.0.6 on 2024-10-19 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_shoporder_shoporderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoporder',
            old_name='user_create',
            new_name='created_user',
        ),
    ]
