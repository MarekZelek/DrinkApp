# Generated by Django 4.0.4 on 2022-06-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FancyDrinks', '0002_alter_drink_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='drink_foto',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
