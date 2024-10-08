# Generated by Django 5.0.6 on 2024-09-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrincipalHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_title', models.CharField(max_length=50, verbose_name='Principal comment')),
                ('secundary_title', models.CharField(max_length=100, verbose_name='Secundary comment')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
            ],
            options={
                'verbose_name': 'SocialMedia',
                'verbose_name_plural': 'SocialMedias',
            },
        ),
        migrations.CreateModel(
            name='WhatsAppContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_whatsapp', models.URLField(max_length=255, verbose_name='Contact whatsapp')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
