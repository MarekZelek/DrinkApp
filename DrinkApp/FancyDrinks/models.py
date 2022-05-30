from django.contrib.auth.models import User
from django.db import models


INGREDIENT_TYPE = (
    (1, "alcohol"),
    (2, "fruit"),
    (4, "sweetener"),
    (3, "other")
)


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    type = models.IntegerField(choices=INGREDIENT_TYPE)
    ingredient_foto = models.ImageField(blank=True, null=True)
    rates = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    drink_foto = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rates = models.IntegerField(default=0)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
