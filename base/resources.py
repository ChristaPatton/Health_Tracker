from import_export import resources
from base.models import Client, Product, Task

class Model1Resource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('entity')

class Model2Resource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('product, latest_available_version')

class Model3Resource(resources.ModelResource):
    class Meta:
        model = Task
        fields = ('client', 'product', 'version', 'last_update', 'note')
