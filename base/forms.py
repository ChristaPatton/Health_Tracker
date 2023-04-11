from django.forms import ModelForm
from .models import Task, Product
from django import forms



    
class ProductForm(forms.ModelForm):
    version = forms.CharField(required=False, widget=forms.TextInput())

    class Meta:
        model = Task
        fields = ['version']
        widgets = {
            'version': forms.TextInput(attrs={'required': False}),
        }

class AddProductForm(forms.ModelForm):
    

    class Meta:
        model = Task
        fields = ['client','product','version']
        
        
class Note(ModelForm):
	note= forms.CharField(widget= forms.Textarea)
	class Meta:
		model = Task
		fields = ['note']

class VersionForm(ModelForm):
    class Meta:
        model = Product
        fields = ['latest_available_version']
        labels = {'latest_available_version': 'The Latest Product Version'}
        widgets = {
            'latest_available_version': forms.TextInput(attrs={'required': False}),
        }
    
       			 
class CapitalizedCharField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if value:
            return value.capitalize()
        return value

class AddForm(forms.ModelForm):
    product = CapitalizedCharField(max_length=100)
    
    class Meta:	
        model = Product
        fields = ['product', 'latest_available_version']
         
      