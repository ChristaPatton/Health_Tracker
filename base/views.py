
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ProductForm, Note, VersionForm, AddForm
from django.urls import reverse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export import resources, fields, widgets
from tablib import Dataset

from .models import Client, Product, Task


def home(request):
    client_list= Client.objects.all().order_by('entity')
    product= Product.objects.all().order_by('product')
    context= {'client_list':client_list, 'product': product}
    return render(request, 'base/home.html', context)

def data_per_client(request, client_id):
    client= Client(pk= client_id)
    data_per_client= Task.objects.filter(client_id=client_id)
    list_client= data_per_client.first()
    context= {'client':client, 'data_per_client': data_per_client, 'list_client': list_client}
    return render(request, 'base/task_list.html', context)

def data_per_product(request, product_id):
    current_version = Product.objects.get(product= product_id)
    the_product1= Product(pk= product_id)
    data_per_product= Task.objects.filter(product_id= product_id)
    one_product=list(Product.objects.filter(id= product_id).values_list("product_item", flat= True))
    context= {'the_product1':the_product1, 'data_per_product': data_per_product, 'one_product':one_product, 'current_version':current_version}
    return render(request, 'base/product_list.html', context)

#the createProduct is really to add a product to one client, the addProduct is to add a new product to the master list
def createProduct(request):
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'base/product_form.html', context)

def updateProduct(request, pk):

	product = Task.objects.get(id=pk)
	form = ProductForm(instance=product)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'base/product_form.html', context)

def deleteProduct(request, pk):
	product = Task.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('/')

	context = {'product':product}
	return render(request, 'base/delete.html', context)


def addNote(request, pk):
	note = Task.objects.get(id=pk)
	form = Note(instance=note)

	if request.method == 'POST':
		form = Note(request.POST, instance=note)
	if form.is_valid():
		form.save()
		return redirect('/')

	context = {'form':form, 'note':note}
	return render(request, 'base/note.html', context)

def delete_note(request, pk):
	note = Task.objects.get(id=pk)
	note.note = None
	note.save()
	if request.method == "POST":
		note.note = None
		note.save()
		return redirect('/')

	context = {'note':note}
	return render(request, 'base/note.html', context)

def master(request):
    masterver= Product.objects.all().order_by('product')

    return render(request, 'base/master.html', {'masterver': masterver})



def updateMaster(request, pk):

	product = Product.objects.get(id=pk)
	form = VersionForm(instance=product)

	if request.method == 'POST':
		form = VersionForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'product': product, 'form':form}
	
	return render(request, 'base/master_form.html', context)


def addProduct(request):
	form = AddForm()
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	
	context = {'form':form}
	return render(request, 'base/master_add_form.html', context)

class Model1Resource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('entity',)

class Model2Resource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('product', 'latest_available_version')

class Model3Resource(resources.ModelResource):
    class Meta:
        model = Task
        fields = ('client', 'product', 'version', 'last_update', 'note')

def import_data(request):
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.FILES['file']
        # Determine which ModelResource to use based on the form data
        resource = None
        model_name = request.POST.get('model_name')
        if model_name == 'Model1':
            resource = Model1Resource()
        elif model_name == 'Model2':
            resource = Model2Resource()
        elif model_name == 'Model3':
            resource = Model3Resource()
        # Use the appropriate ModelResource to import the data
        dataset = Dataset()
        imported_data = dataset.load(file.read(), format='xlsx')
        result = resource.import_data(dataset, dry_run=False)
        if result.has_errors():
            # Handle errors
            pass
        else:
            # Import successful
            pass
    # Render the import form
    context = {'models': ['Model1', 'Model2', 'Model3']}
    return render(request, 'base/import_data.html', context)
