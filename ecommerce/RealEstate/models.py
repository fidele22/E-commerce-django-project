from django.db import models

# Create your models here.

class PhotoCard(models.Model):
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField()

    def __str__(self):
        return self.description
