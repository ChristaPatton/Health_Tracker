
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ProductForm, Note, VersionForm, AddForm, AddProductForm
from django.urls import reverse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export import resources, fields, widgets
from tablib import Dataset
from django.shortcuts import get_object_or_404, redirect, render
from .models import Client, Product, Task
from django.views.decorators.http import require_POST

def home(request):
    client_list= Client.objects.all().order_by('entity')
    product2= Product.objects.all().order_by('product')
    context= {'client_list':client_list, 'product2': product2}
    return render(request, 'base/home.html', context)

def data_per_client(request, client_id):
    client= Client(pk= client_id)
    data_per_client= Task.objects.filter(client_id=client_id).order_by('product')
    
    list_client= data_per_client.first()
    context= {'client':client, 'data_per_client': data_per_client, 'list_client': list_client}
    return render(request, 'base/task_list.html', context)

def data_per_product(request, product):
    current_version = Product.objects.get(product= product)
    the_product1= Product(pk= product)
    data_per_product= Task.objects.filter(product_id= product).order_by('client')
    one_product=list(Product.objects.filter(product= product).values_list("product", flat= True))
    context= {'the_product1':the_product1, 'data_per_product': data_per_product, 'one_product':one_product, 'current_version':current_version}
    return render(request, 'base/product_list.html', context)

#the createProduct is  to add a product to one client, the addProduct is to add a new product to the master list
def createProduct(request):
	form = AddProductForm()
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'base/add_product_form.html', context)

def update_product(request, pk):

	product = Task.objects.get(product=pk)
	form = ProductForm(instance=product)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			
			return redirect('/' )
			
	context = {'form':form, 'product': product}
	return render(request, 'base/product_form.html', context)

#delete product from only one client
def delete_prod(request, pk):
    task = get_object_or_404(Task, product=pk)

    if request.method == "POST":
        task.product.delete()  # Delete the related Product instance
        task.delete()  # Delete the Task instance
        return redirect('/')

    context = {'task': task}
    return render(request, 'base/delete.html', context)

#def deleteProductObject(request, product):


def add_note(request, pk):
	note = Task.objects.get(product=pk)
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

	product = Product.objects.get(product=pk)
	form = VersionForm(instance=product)

	if request.method == 'POST':
		form = VersionForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('master')

	context = {'product': product, 'form':form}
	
	return render(request, 'base/master_form.html', context)

def addProduct(request):
    form = AddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('master')
    
    context = {'form':form}
    return render(request, 'base/master_add.html', context)



#the delet_product deletes a primary key object from the db

def delete_product(request, pk):
    product = get_object_or_404(Product, product=pk)
    
    if request.method == 'POST':
        # If the request method is POST, the user has confirmed the deletion
        product.delete()
        print("Product deleted successfully")
        url = reverse('master')
        print(f"Redirecting to URL: {url}")
        return redirect(url)
    
    # If the request method is GET, show a confirmation page
    context = {'product': product}
    return render(request, 'base/delete_product.html', context)