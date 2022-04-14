from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Place_Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200) #item name
    from_location = models.CharField(max_length=100) #location from which item is picked
    to_location = models.CharField(max_length=100) #location to which item is going
    collect_by_user = models.CharField(max_length=255) #person who colllee ts item
    placed_at = models.DateField(auto_now=True) #date when item was shipped
    order_status = models.CharField(max_length=100, default='on_transit') # on transit, pending or delived.
    # transportation_cost = models.ForeignKey(TransportCost, on_delete = models.CASCADE, blank=True) #should be gotten from  Transportcost depending on the location picked

    # class Meta:
    #     db_table = 'Orders'

    def __str__(self):
        return self.item_name

# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE) #user who is authenticated
#     contact = models.CharField(max_length=100) #phone number
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     adress = models.CharField(max_length=100) #user street adress
#     email = models.EmailField('User Email') #location of the user
#     user_image = models.ImageField(upload_to='media') #user image optional

#     class Meta:
#         db_table = 'UserProfile'

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


class TransportCost(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100) #location 
    to_location = models.CharField(max_length=100) #location
    price = models.IntegerField() #price from location A -B price is example 1000/=
    
    # class Meta:
    #     db_table = 'Orders'

    def __str__(self):
        return self.from_location
