from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import models


from .models import Buyer, Farmer, Product, Purchase, Sale, OwnerDetails
from .forms import BuyerForm, FarmerForm, ProductForm, PurchaseForm, SaleForm, OwnerDetailsForm
from transactions.models import Transaction
from datetime import date
from .utils import get_season_range, get_available_seasons


class LandingPageView(TemplateView):
    template_name = 'core/landing_page.html'

def index(request):
    return render(request, 'kTradersApp/index.html')

def index2(request):
    return render(request, 'kTradersApp/index2.html')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Parse year/season from query params
        year = int(self.request.GET.get('year', date.today().year))
        season = int(self.request.GET.get('season', 1 if date.today().month < 7 else 2))

        season_start, season_end = get_season_range(year, season)

        # Query filtering
        purchases = Purchase.objects.filter(date__range=(season_start, season_end))
        sales = Sale.objects.filter(date__range=(season_start, season_end))

        # Aggregations
        total_purchase_kg = purchases.aggregate(models.Sum('quantity_kg'))['quantity_kg__sum'] or 0
        total_sale_kg = sales.aggregate(models.Sum('quantity_kg'))['quantity_kg__sum'] or 0
        total_purchase_value = purchases.aggregate(total=models.Sum(
            models.F('quantity_kg') * models.F('price_per_kg'),
            output_field=models.DecimalField()))['total'] or 0
        total_sale_value = sales.aggregate(total=models.Sum(
            models.F('quantity_kg') * models.F('price_per_kg'),
            output_field=models.DecimalField()))['total'] or 0

        # Context
        context.update({
            'total_buyers': Buyer.objects.count(),
            'total_farmers': Farmer.objects.count(),
            'total_purchase_kg': total_purchase_kg,
            'total_sale_kg': total_sale_kg,
            'profit': total_sale_value - total_purchase_value,
            'selected_year': year,
            'selected_season': season,
            'available_seasons': get_available_seasons(),
        })
        return context

# Buyer views
class BuyerListView(LoginRequiredMixin, ListView):
    model = Buyer
    template_name = 'core/buyer_list.html'
    context_object_name = 'buyers'

class BuyerCreateView(LoginRequiredMixin, CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('buyer-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Buyer"
        return context

class BuyerUpdateView(LoginRequiredMixin, UpdateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('buyer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Buyer"
        return context


class BuyerDeleteView(LoginRequiredMixin, DeleteView):
    model = Buyer
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('buyer-list')


# Owner views
class OwnerDetailsListView(LoginRequiredMixin, ListView):
    model = OwnerDetails
    template_name = 'core/owner_list.html'
    context_object_name = 'ownerdetails'


class OwnerDetailsCreateView(LoginRequiredMixin, CreateView):
    model = OwnerDetails
    form_class = OwnerDetailsForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('ownerdetails-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Owner Details"
        return context


class OwnerDetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnerDetails
    form_class = OwnerDetailsForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('ownerdetails-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Owner"
        return context


class OwnerDetailsDeleteView(LoginRequiredMixin, DeleteView):
    model = OwnerDetails
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('ownerdetails-list')


# Farmer CRUD
class FarmerListView(LoginRequiredMixin, ListView):
    model = Farmer
    template_name = 'core/farmer_list.html'
    context_object_name = 'farmers'


class FarmerCreateView(LoginRequiredMixin, CreateView):
    model = Farmer
    form_class = FarmerForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('farmer-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Farmer"
        return context


class FarmerUpdateView(LoginRequiredMixin, UpdateView):
    model = Farmer
    form_class = FarmerForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('farmer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Farmer"
        return context


class FarmerDeleteView(LoginRequiredMixin, DeleteView):
    model = Farmer
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('farmer-list')


# Pruducts CRUD
class ProductListView(ListView):
    model = Product
    template_name = 'core/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('product-list')


# Purchase CRUD
class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'core/purchase_list.html'
    context_object_name = 'purchases'


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('purchase-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Purchase"
        return context


class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('purchase-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Purchase"
        return context

class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('purchase-list')


#Sale CRUD
class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'core/sale_list.html'
    context_object_name = 'sales'

class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('sale-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Sale"
        return context

class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('sale-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Sale"
        return context

class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('sale-list')
