from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    image = models.ImageField(upload_to="photos/manufaturers", null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50, null=True)
    brand = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    year = models.IntegerField(null=True)
    body_type = models.CharField(max_length=50, null=True)
    fuel_type = models.CharField(max_length=50, null=True)
    transmission = models.CharField(max_length=50, null=True)
    power = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    top_speed = models.IntegerField(null=True)
    image = models.ImageField(upload_to='photos/cars', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", null=True)

    def __str__(self):
        return self.name
