from typing import Any
from django.db import models

# Create your models here.
class NSID(models.Model):
    '''def __init__(self,image_dir):
        self.image_dir = image_dir'''
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to=f'product')
    description = models.TextField(blank=True)
        
    class Meta:
        abstract = True
    def __str__(self):
        return self.name

class Category(NSID):
    pass    

class Product(NSID):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    


