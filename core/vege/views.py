from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

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

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=email)
        if not user.exists():
            messages.info(request,'Email doesn\'t exist, Please register to proceed.')
            return redirect('/register/')
        else:
            user = authenticate(username=email, password=password)
            if user:
                return redirect('/recipes/')
            else:
                messages.info(request,'Wrong Username/Password')
                return redirect('/login/')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=email)
        if user.exists():
            messages.info(request,'Email already in use')
            return redirect('/register/')

        user = User.objects.create(
            username = email
        )
        user.set_password(password)
        user.save()
        return redirect('/login/')

    return render(request,'register.html')