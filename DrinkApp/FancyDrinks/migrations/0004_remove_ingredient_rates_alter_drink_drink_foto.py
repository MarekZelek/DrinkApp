# Generated by Django 4.0.4 on 2022-06-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FancyDrinks', '0003_alter_drink_drink_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='rates',
        ),
        migrations.AlterField(
            model_name='drink',
            name='drink_foto',
            field=models.ImageField(blank=True, null=True, upload_to='FancyDrinks/static/media/'),
        ),
    ]