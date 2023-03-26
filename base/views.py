
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import ProductForm, Note, VersionForm, AddForm

from .models import Client, Product, Task, Version


def home(request):
    client_list= Client.objects.all().order_by('entity')
    product_list= Product.objects.all().order_by('product_item')
    context= {'client_list':client_list, 'product_list': product_list}
    return render(request, 'base/home.html', context)

def data_per_client(request, client_id):
    client= Client(pk= client_id)
    data_per_client= Task.objects.filter(client_id=client_id)
    list_client= data_per_client.first()
    context= {'client':client, 'data_per_client': data_per_client, 'list_client': list_client}
    return render(request, 'base/task_list.html', context)

def data_per_product(request, product_id):
    current_version = Version.objects.get(the_product= product_id)
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
    masterver= Version.objects.all().order_by('the_product')

    return render(request, 'base/master.html', {'masterver': masterver})

def updateMaster(request, pk):

	the_current_version = Version.objects.get(id=pk)
	form = VersionForm(instance=the_current_version)

	if request.method == 'POST':
		form = VersionForm(request.POST, instance=the_current_version)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'the_current_version': the_current_version, 'form':form}
	
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
