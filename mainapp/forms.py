from django import forms
from .models import UserProfile
from inventory.models import Product, DailyRate
from purchases.models import PurchaseBill, PurchaseItem
from sales.models import SalesBill, SalesItem
from people.models import Buyer, OwnerProfile, Farmer

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
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OwnerProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OwnerProfile
        fields = ['buyer', 'first_name', 'last_name', 'address', 'contact', 'mobile']


class FarmerForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'contact', 'address']


class ProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']


class DailyRateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = DailyRate
        fields = ['product', 'date', 'purchase_rate', 'sales_rate']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'purchase_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'sales_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PurchasesBillForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PurchaseBill
        fields = [  'farmer', 'date', 'purchase_bill_number']


class PurchaseItemForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product', 'sacks', 'weight_kg', 'rate_per_kg']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'sacks': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate_per_kg': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SalesBillForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = SalesBill
        fields = ['buyer', 'vehicle_number', 'transportation_cost', 'date', 'sales_bill_number']


class SalesItemForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = SalesItem
        fields = [ 'sales_bill_number', 'product', 'sacks', 'weight_kg', 'rate_per_kg']


class UserProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['contact', 'profile_pic']


# # class BuyerForm(forms.ModelForm):
# #     class Meta:
# #         model = Buyer
# #         fields = {'company_name', 'pan_num', 'created_by',
# #                   }
# #
# #         widgets = {
# #             'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Buyer Company'}),
# #             'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pan Number'}),
# #             # 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
# #             # 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
# #             # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
# #             # 'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
# #             # 'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
# #             # 'created_by': forms.Select(attrs={'class': 'form-control','id': 'created_by'}),
# #             'created_by': forms.TextInput(attrs={'class': 'form-control', 'id': 'created_by', 'type': 'hidden'}),
# #         }
# #
#
# class EditBuyerForm(forms.ModelForm):
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
# class EditBuyerProfileForm(forms.ModelForm):
#     class Meta:
#         model = OwnerProfile
#         fields = {'first_name', 'last_name', 'address', 'contact', 'mobile' }
#
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
#             'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
#             'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
#             'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
#         }
#
