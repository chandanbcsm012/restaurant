from django.db import models

# Create your models here.
class Customer(models.Model):
    photo = models.ImageField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    date_of_birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length = 30)
    street = models.CharField(max_length = 30)
    zip_code = models.CharField(max_length = 10)
    country = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 15)
    about_me = models.TextField()

class Review(models.Model):
    customer_id = models.IntegerField()
    comment =models.TextField()
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    like = models.IntegerField()
    dislink = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    active = models.BooleanField()
    type = models.CharField(max_length = 20)