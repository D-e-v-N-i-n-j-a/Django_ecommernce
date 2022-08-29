from . import views
from django.urls import path

 

urlpatterns = [
    path('register',views.registerStore,name='registerStore'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('add-product',views.add_product, name='add-product'),
]



  


