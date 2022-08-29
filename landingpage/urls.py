from unicodedata import name
from . import views

from django.urls import path


urlpatterns = [
    path('',views.landingpage,name='landingpage'),
    path('product_details/<str:pk>/',views.product_details,name='product_details'),
]


  


 

