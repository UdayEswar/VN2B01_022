from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    #objects = None
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    Author = models.CharField(max_length=100)
    Creator_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    branch = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name






