from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Products(models.Model):
    product_name = models.CharField(max_length=100,null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    small_image_1 = models.ImageField(upload_to='pics')
    small_image_2 = models.ImageField(upload_to='pics')
    small_image_3 = models.ImageField(upload_to='pics')
    price = models.CharField(max_length=50)
    discount = models.CharField(max_length=50)
    inspired = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    
    def __str__(self):
        return self.product_name



class Reviews(models.Model):
    description = models.TextField()
    date_added =  models.DateTimeField(auto_created=True,auto_now=True)
    product_fk = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
     