from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Drink, Ingredient
from .forms import DrinkForm, IngredientForm, LoginForm, RegistrationForm


class IndexView(View):
    def get(self, request):
        form = DrinkForm()
        drink_list = Drink.objects.all()
        context = {
            'drink_list': drink_list,
            'form': form
        }
        return render(request, 'FancyDrinks/index.html', context)

    # def post(self, request):
    #     form = DrinkForm(request.POST)
    #     if form.is_valid():
    #         Drink.objects.create(
    #             name=form.cleaned_data["name"],
    #             drink_foto=form.cleaned_data["drink_foto"],
    #             description=form.cleaned_data["description"]
    #         )
    #     else:
    #         messages.error(request, "Form is not valid")
    #     return HttpResponseRedirect(reverse('FancyDrinks:index'))


class AddDrinkView(View):
    def get(self, request):
        form = DrinkForm()
        form.owner = request.user.username
        form = DrinkForm(
            initial={
                'rates': 0,
                'owner': form.owner,
            })
        context = {
            'form': form
        }
        return render(request, 'FancyDrinks/add_drink.html', context)

    def post(self, request):
        form = DrinkForm(request.POST, request.FILES)

        if form.is_valid():
            Drink.objects.create(
                name=form.cleaned_data["name"],
                drink_foto=request.FILES["drink_foto"],
                rates=form.cleaned_data['rates'],
                description=form.cleaned_data["description"],
                owner=request.user,
                # how to save many to many from checkbox
                # ingredients.set()
            )
        else:
            messages.error(request, "Form is not valid")
        return HttpResponseRedirect(reverse('FancyDrinks:index'))


class DetailView(LoginRequiredMixin, View):

    def get(self, request, pk):
        # drink = get_object_or_404(Drink, pk=pk)
        drink_form = DrinkForm()
        try:
            # drink = Drink.objects.filter(pk=pk)
            drink = Drink.objects.all().get(pk=pk)
        except Drink.DoesNotExist:
            raise Http404("Drink does not exist")
        context = {
            'drink': drink,
            'drink_form': drink_form,
        }
        return render(request, 'FancyDrinks/detail.html', context)


class EditView(PermissionRequiredMixin, View):
    permission_required = 'FancyDrinks.change_drink'
    raise_exception = True

    def get(self, request, pk):
        drink = get_object_or_404(Drink, pk=pk)
        form = DrinkForm(
            initial={
                'name': drink.name,
                # how to display populated checkboxes
                # 'ingredients': drink.ingredients,
                'description': drink.description,
                'owner': drink.owner,
            }
        )
        context = {
            'drink': drink,
            'form': form
        }
        return render(request, 'FancyDrinks/edit.html', context)

    def post(self, request, pk):
        drink = get_object_or_404(Drink, pk=pk)
        form = DrinkForm(request.POST, request.FILES)
        old_image = Drink.objects.filter()
        if form.is_valid():
            drink.name = form.cleaned_data["name"]
            drink.drink_foto = request.FILES["drink_foto"],
            # drink.ingredients = form.cleaned_data["ingredients"]
            drink.description = form.cleaned_data["description"]
            drink.owner = form.cleaned_data["owner"]
            drink.save()
        return HttpResponseRedirect(reverse('FancyDrinks:detail', args=(drink.id,)))


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                url = request.GET.get('next')
                print(url)
                if url:
                    return redirect(url)
                return HttpResponseRedirect(reverse('FancyDrinks:index'))
            messages.error(request, "Invalid Username or Password")
            return HttpResponseRedirect(reverse('login'))
        messages.error(request, "Form invalid")
        return HttpResponseRedirect(reverse('login'))


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        context = {
            "form": form
        }
        return render(request, 'register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["password_conf"]:
                try:
                    User.objects.get(username=form.cleaned_data["username"])
                    messages.error(request, "User already exists")
                    return HttpResponseRedirect(reverse("registration"))
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        password=form.cleaned_data["password"],
                        email=form.cleaned_data["email"]
                    )
                    group = Group.objects.get(name='standard')
                    user.groups.add(group)
                    login(request, user)
                    return HttpResponseRedirect(reverse("FancyDrinks:index"))
            else:
                messages.error(request, "Passwords are not the same!")
                return HttpResponseRedirect(reverse("registration"))
