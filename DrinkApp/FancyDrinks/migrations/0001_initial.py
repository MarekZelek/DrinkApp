# Generated by Django 4.0.4 on 2022-05-30 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('type', models.IntegerField(choices=[(1, 'alcohol'), (2, 'fruit'), (4, 'sweetener'), (3, 'other')])),
                ('ingredient_foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('rates', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('drink_foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('rates', models.IntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('ingredients', models.ManyToManyField(null=True, to='FancyDrinks.ingredient')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
