from django.db import models

# Create your models here.
class Item(models.Model):

    head = models.CharField(max_length=100)
    image = models.ImageField()
    desc = models.TextField()

    def __str__(self):
        return self.head

class Team(models.Model):

    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name