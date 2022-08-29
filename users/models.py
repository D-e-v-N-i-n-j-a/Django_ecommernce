from itertools import product
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from landingpage.models import Products
# Create your models here.


# CUSTOMER MESSAGE MODELS

class Inbox(models.Model):
    message = models.TextField(null=True)
    date_taken = models.DateField(auto_now_add=True) 
    time_taken = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


class Sender(models.Model):
    message = models.TextField(null=False)
    date_taken = models.DateField(auto_now_add=True) 
    time_taken = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    

class Customers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    




class FavoriteProducts(models.Model):
    product = models.OneToOneField(Products,on_delete=models.CASCADE)
    user = models.OneToOneField(User,null=False,on_delete=models.CASCADE)
    date_added = models.DateTimeField(null=False,auto_now_add=True)
    
    
class PurchaseProduct(models.Model):
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    date_picked = models.DateTimeField(auto_now_add=True)
    date_time = models.TimeField(auto_now_add=True)
    
    


    

     








