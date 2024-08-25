from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def recipes(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        print(request.FILES.get('dish_img'))
        Recipe.objects.create(
            recepe_name = data.get('recipe_name'),
            recipe = data.get('recipe_desc'),
            photo = request.FILES.get('dish_img')
        )
        return redirect('/recipes/')
    queryset = Recipe.objects.all()
    context = {'recipes': queryset}
    return render(request, "recipes.html", context)

def del_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        recepe_name = data.get('recipe_name')
        recipe = data.get('recipe_desc')
        photo = request.FILES.get('dish_img')
        queryset.recepe_name = recepe_name
        queryset.recipe = recipe
        if photo:
            queryset.photo = photo
        queryset.save()
        return redirect('/recipes/')
    context = {'recipe': queryset}
    return render(request, "update_recipes.html", context)