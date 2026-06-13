from rest_framework import serializers
from .models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class RecipeSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(
        source="author.username"
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "ingredients",
            "steps",
            "cooking_time",
            "photo",
            "category",
            "author",
            "author_username",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "author",
            "author_username",
            "created_at",
            "updated_at",
        ]
