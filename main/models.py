from django.db import models

class Item(models.Model):
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    pet = models.CharField(max_length=255)