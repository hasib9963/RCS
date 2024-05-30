from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cheef = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

class Rating(models.Model):
    score = models.IntegerField()
    recipe = models.ForeignKey(Recipe, related_name='ratings', on_delete=models.CASCADE)
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
