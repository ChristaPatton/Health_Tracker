from django.forms import ModelForm
from .models import Task, Product
from django import forms


class ProductForm(ModelForm):
	class Meta:
		model = Task
		fields = ['client','product', 'version']


class Note(ModelForm):
	note= forms.CharField(widget= forms.Textarea)
	class Meta:
		model = Task
		fields = ['note']

class VersionForm(ModelForm):
	

	class Meta:
		model = Product
		fields = ['product']
		labels= {'product': 'The Latest Version'}

class AddForm(ModelForm):
	class Meta:	
		model = Product
		fields = ['product']
