from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TransportCost(models.Model):
    from_location = models.CharField(max_length=100) #location 
    to_location = models.CharField(max_length=100) #location
    price = models.IntegerField() #price from location A -B price is example 1000/=

    # class Meta:
    #     db_table = 'Orders'

    def __str__(self):
        return self.from_location

class Place_Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,  related_name='place_Order') #user whpo add item
    item_name = models.CharField(max_length=200) #item name
    from_location = models.CharField(max_length=100) #location from which item is picked
    to_location = models.CharField(max_length=100) #location to which item is going
    collect_by_user = models.CharField(max_length=100) #person who colllee ts item
    # collect_by_userid = models.IntegerField() #id of user who collects item
    placed_at = models.DateField(auto_now=True) #date when item was shipped
    collect_at = models.DateField(auto_now=True) #date which item should be picked
    order_status = models.CharField(max_length=100, default='Pending') # on transit, pending or delived.
    transportation_cost = models.ForeignKey(TransportCost, on_delete = models.CASCADE) #should be gotten from  Transportcost depending on the location picked

    # class Meta:
    #     db_table = 'Orders'

    def __str__(self):
        return self.item_name

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) #user who is authenticated
    contact = models.CharField(max_length=100) #phone number
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=100) #user street adress
    email = models.EmailField('User Email') #location of the user
    user_image = models.ImageField(upload_to='media') #user image optional

    class Meta:
        db_table = 'UserProfile'

    def __str__(self):
        return self.first_name + ' ' + self.last_name