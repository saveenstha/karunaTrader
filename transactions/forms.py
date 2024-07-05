from django import forms
from transactions.models import Transaction #, ParticularsDetail


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = {'bill_number','buyer','transaction_type', 'amount'}

        widget = {

            'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Bill Number'}),
            'buyer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter PAN Number'}),
            'transaction_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose Transaction Type'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Amount'}),
        }


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