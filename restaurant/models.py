from django.db import models

# Create your models here.
class Restaurant(models.Model):
    photo = models.ImageField(upload_to="restaurant")
    name = models.CharField(max_length=30)
    established = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    people = models.CharField(max_length=30)
    website = models.URLField(max_length = 30)
    address = models.TextField()
    city = models.CharField(max_length = 30 )
    state = models.CharField(max_length = 30 )
    street = models.CharField(max_length = 30)
    zip_code = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30 )
    company_background = models.TextField()
    services = models.TextField()
    expertise = models.TextField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    restaurant_name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to="dish")

    def __str__(self):
        return self.name