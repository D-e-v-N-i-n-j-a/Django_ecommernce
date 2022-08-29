from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Store(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_created = models.BooleanField()
    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.store_name