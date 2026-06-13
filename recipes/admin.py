from django.contrib import admin
from .models import Category, Recipe

class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RecipeInline]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ('title', 'description''author','category',)
    list_filter = ('category', 'created_at')
    readonly_fields = ('created_at', 'updated_at')



