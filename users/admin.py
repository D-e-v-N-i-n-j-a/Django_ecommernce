from django.contrib import admin
from .models import Inbox,Sender,Customers,FavoriteProducts
# from . models import Profile
# Register your models here.


admin.site.register(Inbox) 
admin.site.register(Sender) 
admin.site.register(Customers) 
admin.site.register(FavoriteProducts) 
  