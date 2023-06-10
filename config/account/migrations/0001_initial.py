# Generated by Django 4.2.2 on 2023-06-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='John',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('telegram_link', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=200, null=True)),
                ('is_moderator', models.BooleanField(blank=True, default=False, null=True)),
                ('points', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
