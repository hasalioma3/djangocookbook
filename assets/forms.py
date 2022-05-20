from django.forms import ModelForm
from django import forms
from .models import Categories, Assets

# create a form class for the model
class AssetForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'description', 'category', 'price', 'serial_No', 'barcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'serial_No': forms.TextInput(attrs={'class': 'form-control'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control'}),

        }

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
