from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PurchaseBill, PurchaseItem
from inventory.models import *
from mainapp.forms import *


# Purchase CRUD
class PurchaseBillListView(LoginRequiredMixin, ListView):
    model = PurchaseBill
    template_name = 'mainapp/purchasebill_list.html'
    context_object_name = 'purchases'
    paginate_by = 10

    def get_queryset(self):
        return PurchaseBill.objects.all().order_by('-purchase_bill_number') # Replace 'field_name'


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


class PurchaseItemCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseItem
    form_class = PurchaseItemForm
    template_name = 'purchases/purchaseitem_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.purchase_bill = get_object_or_404(PurchaseBill, pk=kwargs['bill_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.purchase_bill_number = self.purchase_bill

        # Automatically set rate from DailyRate if available
        rate = DailyRate.objects.filter(product=form.instance.product, date=self.purchase_bill.date).first()
        if rate:
            form.instance.rate_per_kg = rate.purchase_rate

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_bill'] = self.purchase_bill
        return context

    def get_success_url(self):
        return reverse('people:farmer-profile', args=[self.purchase_bill.farmer.id])


class PurchaseItemEditView(LoginRequiredMixin, UpdateView):
    model = PurchaseItem
    form_class = PurchaseItemForm
    template_name = 'purchases/purchaseitem_edit_formset.html'

    def form_valid(self, form):
        # Optional: Update rate dynamically based on date/product change
        purchase_bill = form.instance.purchase_bill_number
        rate = DailyRate.objects.filter(product=form.instance.product, date=purchase_bill.date).first()
        if rate:
            form.instance.rate_per_kg = rate.purchase_rate
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('farmers:farmer-profile', kwargs={
            'pk': self.object.purchase_bill_number.farmer.pk
        })


class PurchaseItemDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchaseItem
    template_name = 'purchases/purchaseitem_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('farmers:farmer-profile', kwargs={
            'pk': self.object.purchase_bill_number.farmer.pk
        })
