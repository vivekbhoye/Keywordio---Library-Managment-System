from django.urls import reverse
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=50)
    no_of_pages = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} Book'

    def get_absolute_url(self):
        return reverse('home')