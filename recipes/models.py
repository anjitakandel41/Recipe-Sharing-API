from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    ingredients=models.TextField()
    steps=models.TextField()
    cooking_time=models.PositiveIntegerField()
    photo=models.ImageField(upload_to='recipes/',blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
