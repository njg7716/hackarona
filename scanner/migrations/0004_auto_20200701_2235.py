# Generated by Django 2.1.15 on 2020-07-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_auto_20200701_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanphoto',
            name='scan',
            field=models.ImageField(upload_to=''),
        ),
    ]
