from django.db import models

# Create your models here.

class Foods(models.Model):
    name= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    material= models.TextField()
    how= models.TextField()
    time= models.CharField(max_length=50)
    points= models.TextField(default=" ")

    
    def __str__(self):
        return self.name
        