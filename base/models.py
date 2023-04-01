from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    entity = models.CharField(primary_key= True, max_length= 200)

    def __str__(self):
        return self.entity

class Product(models.Model):
    product = models.CharField(primary_key= True, unique= True, max_length= 200)
    latest_available_version =  models.CharField(max_length= 200, null= True)
    def __str__(self):
        return self.product

class Task(models.Model):
    
    client = models.ForeignKey(Client, related_name= 'tasks', on_delete= models.CASCADE, null= True, blank=True)
    product = models.ForeignKey(Product, related_name= 'tasks', on_delete=models.CASCADE, null=True, blank= True, to_field= 'product')
    version = models.CharField(max_length= 200, null= True)
    last_update = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=250, null= True)
    

    def __str__(self):
        return str(self.client)


    class Meta:
        ordering = ['client']

