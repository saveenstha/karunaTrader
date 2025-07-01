from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import models

from people.models import *
from mainapp.forms import *


# Buyer views
class BuyerListView(LoginRequiredMixin, ListView):
    model = Buyer
    template_name = 'people/buyer_list.html'
    context_object_name = 'buyers'


class BuyerCreateView(LoginRequiredMixin, CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'people/buyer_form.html'
    success_url = reverse_lazy('people:buyer-list')

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
    template_name = 'people/buyer_form.html'
    success_url = reverse_lazy('people:buyer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Buyer"
        return context


class BuyerDeleteView(LoginRequiredMixin, DeleteView):
    model = Buyer
    template_name = 'mainapp/confirm_delete.html'
    success_url = reverse_lazy('people:buyer-list')


class BuyerProfileView(LoginRequiredMixin, DetailView):
    model = Buyer
    template_name = 'people/buyer_profile.html'
    context_object_name = 'buyer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_bills'] = SalesBill.objects.filter(buyer=self.object).order_by('-date')
        return context


# OwnerProfile CRUD
class OwnerProfilesListView(LoginRequiredMixin, ListView):
    model = OwnerProfile
    template_name = 'people/ownerprofile_list.html'
    context_object_name = 'ownerprofiles'


class OwnerProfilesCreateView(LoginRequiredMixin, CreateView):
    model = OwnerProfile
    form_class = OwnerProfileForm
    template_name = 'people/ownerprofile_form.html'
    success_url = reverse_lazy('ownerprofiles-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Owner Details"
        return context


class OwnerProfilesUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnerProfile
    form_class = OwnerProfileForm
    template_name = 'people/ownerprofile_form.html'
    success_url = reverse_lazy('ownerprofiles-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Owner"
        return context


class OwnerProfilesDeleteView(LoginRequiredMixin, DeleteView):
    model = OwnerProfile
    template_name = 'mainapp/confirm_delete.html'
    success_url = reverse_lazy('ownerprofiles-list')


# Farmer CRUD
class FarmerListView(LoginRequiredMixin, ListView):
    model = Farmer
    template_name = 'people/farmer_list.html'
    context_object_name = 'farmers'


class FarmerCreateView(LoginRequiredMixin, CreateView):
    model = Farmer
    form_class = FarmerForm
    template_name = 'people/farmer_form.html'
    success_url = reverse_lazy('people:farmer-list')

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
    template_name = 'people/farmer_form.html'
    success_url = reverse_lazy('people:farmer-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Farmer"
        return context


class FarmerDeleteView(LoginRequiredMixin, DeleteView):
    model = Farmer
    template_name = 'people/confirm_delete.html'
    success_url = reverse_lazy('people:farmer-list')


class FarmerProfileView(LoginRequiredMixin, DetailView):
    model = Farmer
    template_name = 'people/farmer_profile.html'
    context_object_name = 'farmer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchase_bills'] = PurchaseBill.objects.filter(farmer=self.object).order_by('-date')
        return context