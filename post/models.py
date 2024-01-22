from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    
    # making relationships
    category = models.ManyToManyField(Category) # A post could be create by many categories and also Many post could be create base on a category. so this is many to many relationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'
