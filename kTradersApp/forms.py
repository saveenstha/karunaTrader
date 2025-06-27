from django import forms
from .models import Buyer, OwnerDetails, Farmer, Product, Purchase, Sale

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = 'form-check-input'
            field.widget.attrs.update({'class': css_class})


class BuyerForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['company_name', 'pan_num', 'balance']

class OwnerDetailsForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OwnerDetails
        fields = '__all__'

class FarmerForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'contact', 'address']

class ProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

class PurchaseForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['farmer', 'product', 'quantity_kg', 'price_per_kg', 'date']

class SaleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['buyer', 'product', 'quantity_kg', 'price_per_kg', 'transport_charge', 'billing_info', 'date']

#
# class BuyerForm(forms.ModelForm):
#     class Meta:
#         model = Buyer
#         fields = {'company_name', 'pan_num', 'created_by',
#                   }
#
#         widgets = {
#             'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Buyer Company'}),
#             'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pan Number'}),
#             # 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
#             # 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
#             # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
#             # 'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
#             # 'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
#             # 'created_by': forms.Select(attrs={'class': 'form-control','id': 'created_by'}),
#             'created_by': forms.TextInput(attrs={'class': 'form-control', 'id': 'created_by', 'type': 'hidden'}),
#         }
#

class EditBuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = {'company_name', 'pan_num', 'created_by',
                  }

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Buyer Company'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pan Number'}),
            # 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            # 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            # 'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            # 'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            # 'created_by': forms.Select(attrs={'class': 'form-control','id': 'created_by'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'id': 'created_by', 'type': 'hidden'}),
        }
class EditBuyerProfileForm(forms.ModelForm):
    class Meta:
        model = OwnerDetails
        fields = {'first_name', 'last_name', 'address', 'contact', 'mobile' }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
        }

