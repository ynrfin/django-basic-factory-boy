from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey( 
        'Category', 
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
