from atexit import register
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LOCATION_CHOICES = (('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Embu', 'Embu'), ('Nakuru', 'Nakuru'))
    pickup_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    destination_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    sender_contact = models.CharField(max_length=200)
    receipient_name = models.CharField(max_length=200)
    receipient_contact = models.CharField(max_length=200)
    PACKAGE_CHOICES = (('Small', 'Small'), ('Large', 'Large'))
    parcel_package = models.CharField(max_length=100, choices=PACKAGE_CHOICES)
    
    def __str_(self):
        return self.first_name + ' ' + self.last_name

class Sender(models.Model):
    sender_name = models.CharField(max_length=200)

    def __str_(self):
        return self

class newdestination(models.Model):
    LOCATION_CHOICES = (('N', 'Nairobi'), ('M', 'Mombasa'), ('K', 'Kisumu'), ('E', 'Embu'), ('N', 'Nakuru'))
    new_location = models.CharField(max_length=1, choices=LOCATION_CHOICES)

    def __str_(self):
        return self

class Cost(models.Model):
    from_location = models.CharField(max_length=255, default='from-location')
    to_location = models.CharField(max_length=255, default='to-location')
    price = models.IntegerField()
