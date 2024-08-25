from django.db import models

# Create your models here.

class Recipe(models.Model):
    recepe_name = models.CharField(max_length=200)
    recipe = models.TextField()
    photo = models.ImageField(upload_to="recipeImages")