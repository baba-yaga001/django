from django.db import models

# Create your models here.

class cntry(models.Model):

    name = models.CharField(max_length=50)
    about = models.TextField()
    img  = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name