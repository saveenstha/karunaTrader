from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PurchaseBill, PurchaseItem
from inventory.models import *
from mainapp.forms import *


# Purchase CRUD
class PurchaseBillListView(LoginRequiredMixin, ListView):
    model = PurchaseBill
    template_name = 'mainapp/purchasebill_list.html'
    context_object_name = 'purchases'


class PurchaseBillCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseBill
    form_class = PurchasesBillForm
    template_name = 'purchases/purchasebill_form.html'
    success_url = reverse_lazy('purchases:purchasebill-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ItemFormSet = inlineformset_factory(PurchaseBill, PurchaseItem, form=PurchaseItemForm, extra=1, can_delete=False)
        context['page_title'] = "Add Purchase"
        if self.request.POST:
            context['formset'] = ItemFormSet(self.request.POST)
        else:
            context['formset'] = ItemFormSet()
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
                        item_form.instance.rate = rate.purchase_rate
            formset.save()
            return redirect(self.success_url)
        return self.form_invalid(form)


class PurchaseBillUpdateView(LoginRequiredMixin, UpdateView):
    model = PurchaseBill
    form_class = PurchasesBillForm
    template_name = 'mainapp/form.html'
    success_url = reverse_lazy('purchases:purchasebill-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Purchase"
        return context


class PurchaseBillDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchaseBill
    template_name = 'mainapp/confirm_delete.html'
    success_url = reverse_lazy('purchase-list')
