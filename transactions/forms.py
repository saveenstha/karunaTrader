from django import forms
from transactions.models import Transaction #, ParticularsDetail


# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = {'txn_date','bill_number', 'pan_num', 'credit_amount'}
#
#         widget = {
#             'txn_date': forms.DateInput(format=('%Y-%m-%d'),
#                                         attrs={'class': 'form-control dateinput form-control',
#                                                'placeholder': 'Select a date'}),
#             'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
#             'pan_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PAN Number'}),
#             'credit_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Amount'}),
#         }


# class ParticularsForm(forms.ModelForm):
#     class Meta:
#         model = ParticularsDetail
#         fields = {'txn_date', 'bill_number', 'particulars', 'quantity', 'rate', 'goods_amount','transport_vehicle', 'driver_contact',
#                   'total_package', 'fare_per_package_rate', 'labour_cost', 'total_amount',
#                   }
#
#         widgets = {
#             'txn_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input'}),
#             'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
#             'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter particulars'}),
#             'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
#             'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter rate'}),
#             'goods_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Goods'}),
#             'transport_vehicle': forms.TextInput(attrs={'class':'form-control'}),
#             'driver_contact': forms.TextInput(attrs={'class':'form-control'}),
#             'total_package': forms.TextInput(attrs={'class':'form-control'}),
#             'fare_per_package_rate': forms.TextInput(attrs={'class':'form-control'}),
#             'labour_cost': forms.TextInput(attrs={'class':'form-control'}),
#             'total_amount': forms.TextInput(attrs={'class':'form-control'}),
#         }