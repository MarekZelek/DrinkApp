from django import forms

from .models import Drink, Ingredient, INGREDIENT_TYPE


class IngredientForm(forms.Form):
    name = forms.CharField(label="name")
    type = forms.ChoiceField(choices=INGREDIENT_TYPE, label="type")
    ingredient_foto = forms.ImageField(label="foto", required=False)


class DrinkForm(forms.Form):
    name = forms.CharField(label="name")
    ingredients = forms.ModelMultipleChoiceField(label="ingredients", queryset=Ingredient.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple
                                                 )
    drink_foto = forms.ImageField(label="drink foto")
    rates = forms.CharField(label="Initial rates number", required=False)
    description = forms.CharField(
        widget=forms.Textarea, label="Description")
    owner = forms.CharField(label="owner", disabled=True)


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
