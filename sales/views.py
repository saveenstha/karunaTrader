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
            total_bill = 0
            for item_form in formset:
                if item_form.cleaned_data.get("product"):
                    product = item_form.cleaned_data["product"]
                    rate = DailyRate.objects.filter(product=product, date=bill.date).first()
                    if rate:
                        item_form.instance.rate = rate.sales_rate
                    total_bill += item_form.cleaned_data['weight_kg'] * item_form.cleaned_data['rate_per_kg']
            formset.save()

            # Update buyer balance
            bill.buyer.balance += total_bill
            bill.buyer.save()
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
        previous_total = sum(item.total_price() for item in self.object.items.all())

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
            new_total = sum(item.total_price() for item in self.object.items.all())
            diff = new_total - previous_total

            self.object.buyer.balance += diff
            self.object.buyer.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class SalesBillDeleteView(LoginRequiredMixin, DeleteView):
    model = SalesBill
    template_name = 'mainapp/confirm_delete.html'
    # template_name = 'sales/salesbill_confirm_delete.html'


class SalesItemCreateView(LoginRequiredMixin, CreateView):
    model = SalesItem
    form_class = SalesItemForm
    template_name = 'sales/salesitem_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.sales_bill = get_object_or_404(salesBill, pk=kwargs['bill_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.sales_bill_number = self.sales_bill

        # Automatically set rate from DailyRate if available
        rate = DailyRate.objects.filter(product=form.instance.product, date=self.sales_bill.date).first()
        if rate:
            form.instance.rate_per_kg = rate.sales_rate

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_bill'] = self.sales_bill
        return context

    def get_success_url(self):
        return reverse('people:farmer-profile', args=[self.sales_bill.farmer.id])


class SalesItemEditView(LoginRequiredMixin, UpdateView):
    model = SalesItem
    form_class = SalesItemForm
    template_name = 'sales/salesitem_edit_formset.html'

    def post(self, request, pk):
        item = get_object_or_404(SalesItem, pk=pk)
        form = SalesItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('buyers:buyer-profile', pk=item.sales_bill_number.buyer.pk)

    def form_valid(self, form):
        # Optional: Update rate dynamically based on date/product change
        sales_bill = form.instance.sales_bill_number
        rate = DailyRate.objects.filter(product=form.instance.product, date=sales_bill.date).first()
        if rate:
            form.instance.rate_per_kg = rate.sales_rate
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('people:buyer-profile', kwargs={
            'pk': self.object.sales_bill_number.farmer.pk
        })


class SalesItemDeleteView(LoginRequiredMixin, DeleteView):
    model = SalesItem
    template_name = 'saless/salesitem_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('people:buyer-profile', kwargs={
            'pk': self.object.sales_bill_number.farmer.pk
        })
