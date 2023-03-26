from django.forms import ModelForm
from .models import Task, Version, Product
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
	
	model = Version
	class Meta:
		model = Version
		fields = ['the_current_version']
		labels= {'the_current_version': 'The Latest Version'}

class AddForm(ModelForm):
	class Meta:	
		model = Product
		fields = ['product_item']
