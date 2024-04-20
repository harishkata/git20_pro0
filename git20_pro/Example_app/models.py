from django.db import models

# Create your models here.

class Example(models.model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()