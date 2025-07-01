from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.utils.timezone import make_aware

import calendar
from calendar import Calendar, month_name
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta

from .models import Product, DailyRate
from mainapp.forms import ProductForm, DailyRateForm


# Product views
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('inventory:product-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Product"
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('inventory:product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Product"
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'mainapp/confirm_delete.html'
    success_url = reverse_lazy('inventory:product-list')


# Daily Rate CRUD
class DailyRateListView(LoginRequiredMixin, ListView):
    model = DailyRate
    template_name = 'inventory/dailyrate_list.html'
    context_object_name = 'dailyrates'


class DailyRateCreateView(LoginRequiredMixin, CreateView):
    model = DailyRate
    form_class = DailyRateForm
    template_name = 'inventory/dailyrate_form.html'
    success_url = reverse_lazy('inventory:dailyrate-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add dailyrate"
        return context


class DailyRateUpdateView(LoginRequiredMixin, UpdateView):
    model = DailyRate
    form_class = DailyRateForm
    template_name = 'inventory/dailyrate_form.html'
    success_url = reverse_lazy('inventory:dailyrate-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit dailyrate"
        return context


class DailyRateDeleteView(LoginRequiredMixin, DeleteView):
    model = DailyRate
    template_name = 'mainapp/confirm_delete.html'
    success_url = reverse_lazy('inventory:dailyrate-list')


class RateCalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/rate_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')

        today = date.today()
        year = int(year) if year else today.year
        month = int(month) if month else today.month

        cal = Calendar(firstweekday=6)
        month_dates = list(cal.itermonthdates(year, month))
        weeks = [month_dates[i:i + 7] for i in range(0, len(month_dates), 7)]

        # Month navigation helpers
        prev_month = month - 1 if month > 1 else 12
        prev_year = year - 1 if month == 1 else year
        next_month = month + 1 if month < 12 else 1
        next_year = year + 1 if month == 12 else year

        # Map {date: [rates]}
        rate_map = {day: DailyRate.objects.filter(date=day) for day in month_dates}


        context.update({
            'weeks': weeks,
            'rate_map': rate_map,
            'month_name': month_name[month],
            'month': month,
            'year': year,
            'weekdays': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
            'prev_year': prev_year,
            'prev_month': prev_month,
            'next_year': next_year,
            'next_month': next_month,
        })
        return context

