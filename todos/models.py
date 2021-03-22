from django.db import models


# Create your models here.

class Todo(models.Model):
    name=models.CharField(max_length=64)
    task=models.CharField(max_length=100)
    due=models.CharField(max_length=10)
    email=models.EmailField()


    def __str__(self):
        return  self.name
