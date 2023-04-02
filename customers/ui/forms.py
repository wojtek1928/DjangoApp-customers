from django import forms
from django.forms import ModelForm
from ..models import Customer, PostalAddress


# Postal address form
class PostalAddressAddForm(ModelForm):
    class Meta:
        model = PostalAddress
        fields = ['street', 'house_number',
                  'apartment_number', 'city', 'postal_code']

        # Deleted labels are replaced with placeholders
        labels = {
            'street': '',
            'house_number': '',
            'apartment_number': '',
            'city': '',
            'postal_code': ''
        }
        # Setting bootstrap classes for fields and adding placeholders
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House number'}),
            'apartment_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal code'}),
        }


# Create a customer add form
class CustomerAddForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'vat_id_number']
        # Deleted labels are replaced with placeholders
        labels = {
            'name': '',
            'vat_id_number': ''
        }
        # Setting bootstrap classes for fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'vat_id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PLXXXXXXXXXX'}),
        }


# Create a customer edit form
class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'vat_id_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'vat_id_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Create a postal address edit form
class PostalAddressEditForm(forms.ModelForm):
    class Meta:
        model = PostalAddress
        fields = ['street', 'house_number',
                  'apartment_number', 'city', 'postal_code']
        # Setting bootstrap classes for fields
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'apartment_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
