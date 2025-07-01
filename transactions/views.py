from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Transaction
from .forms import TransactionForm
from django.contrib import messages
from django.views import generic
from django.views.generic import CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.

class AddTransactionView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/add_transaction.html'
    # success_url = 'dashboard'

    def form_valid(self, form):
        response = super().form_valid(form)
        transaction = form.instance
        buyer = transaction.buyer

        if transaction.transaction_type == 'credit':
            buyer.balance += transaction.amount
        elif transaction.transaction_type == 'debit':
            buyer.balance -= transaction.amount

        buyer.save()
        return response


class DeleteTransactionViews(generic.DeleteView):
    model = Transaction
    template_name = "transactions/delete_transaction.html"
    success_url = reverse_lazy('dashboard')

# class AddParticularsView(CreateView):
#     model = ParticularsDetail
#     form_class = ParticularsForm
#     template_name = 'mainapp/buyer/add_particulars.html'
