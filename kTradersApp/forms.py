from django import forms
from .models import Buyer, OwnerDetails

class BuyerForm(forms.ModelForm):
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

