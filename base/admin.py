from django.contrib import admin
from .models import Task, Client, Product, Version
# Register your models here.
admin.site.register(Task)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Version)