from django.db import models

# Create your models here.
from django.db import models

class PhotoCard(models.Model):
    photo = models.ImageField(upload_to='photos/')
    name = models.TextField(default="Default Name")
    type = models.TextField(default="Default Type")
    price = models.CharField(max_length=200, default="Default Price")
    delivery_time = models.TextField(default="Default Delivery Time")
    delivery_cost = models.CharField(max_length=200, default="Default Delivery Cost")

    def __str__(self):
        return self.name

