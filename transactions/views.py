from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Transaction
from kTradersApp.models import Buyer
# from .forms import TransactionForm
from django.contrib import messages
from django.views import generic
from django.views.generic import CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.

class AddTransactionView(CreateView):
    model = Transaction
    # form_class = TransactionForm
    template_name = 'transactions/add_transaction.html'
    # success_url = 'dashboard'

    def form_valid(self, form):
        txn = form.save(commit=False)
        previous_balance = Buyer.objects.filter(pan_num=form.instance.pan_num).value("Balance")
        print("form instance pan num: ", form.instance.pan_num)
        print("Previous balance :", previous_balance)
        print("form value :", form.instance.credit_amount)
        # txn.balance_after_transaction = previous_balance + form.instance.credit_amount
        # new_balance = previous_balance + form.instance.credit_amount

        # print("new balance :", new_balance)
        txn.save()
        return super(AddTransactionView, self).form_valid(form)


class DeleteTransactionViews(generic.DeleteView):
    model = Transaction
    template_name = "transactions/delete_transaction.html"
    success_url = reverse_lazy('dashboard')

# class AddParticularsView(CreateView):
#     model = ParticularsDetail
#     form_class = ParticularsForm
#     template_name = 'kTradersApp/buyer/add_particulars.html'
