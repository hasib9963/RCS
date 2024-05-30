from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe, Ingredient, Rating, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'author', 'ingredients', 'ratings', 'comments']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity', 'unit']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'score', 'rated_by']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'commented_by']
