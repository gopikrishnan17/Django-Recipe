from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recepe_name = models.CharField(max_length=200)
    recipe = models.TextField()
    photo = models.ImageField(upload_to="recipeImages")