# Generated by Django 3.2.6 on 2023-07-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20230701_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='doned_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
