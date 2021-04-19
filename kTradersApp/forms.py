from django import forms
from .models import Buyer, Transaction, ParticularsDetail

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = {'company_name', 'pan_num', 'first_name', 'last_name', 'address', 'contact', 'mobile', 'created_by',
                  }

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Buyer Company'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pan Number'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            # 'created_by': forms.Select(attrs={'class': 'form-control','id': 'created_by'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'id': 'created_by', 'type': 'hidden'}),
        }


class EditBuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = {'company_name', 'pan_num', 'first_name', 'last_name', 'address', 'contact', 'mobile', 'created_by',
                  }

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of Buyer Company'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pan Number'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            # 'created_by': forms.Select(attrs={'class': 'form-control','id': 'created_by'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'id': 'created_by', 'type': 'hidden'}),
        }


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = {'txn_date', 'bill_number', 'pan_num', 'total_amount', 'transport_vehicle', 'driver_contact', 'vehicle_fare',
                  }

        widget = {
            'txn_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input'}),
            'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
            'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PAN Number'}),
            'total_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Amount'}),
            'transport_vehicle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Transportation Vehicle Number'}),
            'driver_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Driver's Mobile Number"}),
            'vehicle_fare': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Vehicle Fare'}),
        }


class AddParticularsForm(forms.ModelForm):
    class Meta:
        modal = ParticularsDetail
        fields = {'bill_number', 'particulars', 'quantity', 'rate', 'goods_amount'}

        widgets = {
            'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
            'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter particulars'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
            'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
            'goods_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
        }