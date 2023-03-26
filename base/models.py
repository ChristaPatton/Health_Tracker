from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    entity = models.CharField(max_length= 200)

    def __str__(self):
        return self.entity

class Product(models.Model):
    product_item = models.CharField(max_length= 200, null= True)

    def __str__(self):
        return self.product_item

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, related_name= 'tasks', on_delete= models.CASCADE, null= True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank= True)
    version = models.CharField(max_length= 200, null= True)
    current_version = models.CharField(max_length= 200, null = True)
    last_update = models.DateTimeField(auto_now=True)
    note = models.CharField(max_length=250, null= True)
    

    def __str__(self):
        return str(self.client)


    class Meta:
        ordering = ['client']

class Version(models.Model):
    the_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank= True)
    the_current_version= models.CharField(max_length= 250, null= True) 

    def __str__(self):
        return str(self.the_product)