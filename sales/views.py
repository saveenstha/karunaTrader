from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db import models

from mainapp.forms import *
from .models import SalesBill, SalesItem
from inventory.models import DailyRate


#Sale CRUD
class SalesBillListView(LoginRequiredMixin, ListView):
    model =  SalesBill
    template_name = 'mainapp/salesbill_list.html'
    context_object_name = 'salesbills'


# class SalesBillCreateView(LoginRequiredMixin, CreateView):
#     model =  SalesBill
#     form_class = SalesBillForm
#     template_name = 'mainapp/form.html'
#     success_url = reverse_lazy('sale-list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = "Add Sale"
#         return context


# === views.py snippet for sales bill creation ===
class SalesBillCreateView(View):
    def get(self, request):
        bill_form = SalesBillForm()
        ItemFormSet = inlineformset_factory(SalesBill, SalesItem, form=SalesItemForm, extra=1, can_delete=False)
        formset = ItemFormSet()
        return render(request, 'sales/salesbill_form.html', {'form': bill_form, 'formset': formset})

    def post(self, request):
        bill_form = SalesBillForm(request.POST)
        ItemFormSet = inlineformset_factory(SalesBill, SalesItem, form=SalesItemForm, extra=1, can_delete=False)
        formset = ItemFormSet(request.POST)

        if bill_form.is_valid() and formset.is_valid():
            bill = bill_form.save()
            formset.instance = bill
            for item_form in formset:
                if item_form.cleaned_data.get("product"):
                    product = item_form.cleaned_data["product"]
                    rate = DailyRate.objects.filter(product=product, date=bill.date).first()
                    if rate:
                        item_form.instance.rate = rate.rate
            formset.save()
            return redirect('sales:salesbill-list')
        return render(request, 'sales/salesbill_form.html', {'form': bill_form, 'formset': formset})


class SalesBillUpdateView(LoginRequiredMixin, UpdateView):
    model =  SalesBill
    form_class = SalesBillForm
    template_name = 'sales/salesbill_form.html'
    success_url = reverse_lazy('sales:salesbill-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ItemFormSet = inlineformset_factory(SalesBill, SalesItem, form=SalesItemForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset'] = ItemFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = ItemFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            for item_form in formset:
                if item_form.cleaned_data.get("product"):
                    product = item_form.cleaned_data["product"]
                    rate = DailyRate.objects.filter(product=product, date=self.object.date).first()
                    if rate:
                        item_form.instance.rate = rate.sales_rate
            formset.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class SalesBillDeleteView(LoginRequiredMixin, DeleteView):
    model = SalesBill
    template_name = 'mainapp/confirm_delete.html'
    template_name = 'sales/salesbill_confirm_delete.html'