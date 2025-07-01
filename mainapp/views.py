from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db import models

from .models import *
from .forms import *
# from transactions.models import Transaction
from datetime import date
from .utils import get_season_range, get_available_seasons
from people.models import Buyer, Farmer
# from purchases.models import PurchaseBill
# from sales.models import SalesBill

User = get_user_model()


class LandingPageView(TemplateView):
    template_name = 'mainapp/landing_page.html'

def index(request):
    return render(request, 'mainapp/index.html')

def index2(request):
    return render(request, 'mainapp/index2.html')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'mainapp/dashboard.html'
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Parse year/season from query params
        year = int(self.request.GET.get('year', date.today().year))
        season = int(self.request.GET.get('season', 1 if date.today().month < 7 else 2))

        season_start, season_end = get_season_range(year, season)

        # Query filtering
    #     purchases = PurchaseBill.objects.filter(date__range=(season_start, season_end))
    #     sales = SalesBill.objects.filter(date__range=(season_start, season_end))
    #
        # Aggregations
    #     total_purchase_kg = purchases.aggregate(models.Sum('quantity_kg'))['quantity_kg__sum'] or 0
    #     total_sale_kg = sales.aggregate(models.Sum('quantity_kg'))['quantity_kg__sum'] or 0
    #     total_purchase_value = purchases.aggregate(total=models.Sum(
    #         models.F('quantity_kg') * models.F('price_per_kg'),
    #         output_field=models.DecimalField()))['total'] or 0
    #     total_sale_value = sales.aggregate(total=models.Sum(
    #         models.F('quantity_kg') * models.F('price_per_kg'),
    #         output_field=models.DecimalField()))['total'] or 0
    #
    #     # Context
        context.update({
            'total_buyers': Buyer.objects.count(),
            'total_farmers': Farmer.objects.count(),
    #         'total_purchase_kg': total_purchase_kg,
    #         'total_sale_kg': total_sale_kg,
    #         'profit': total_sale_value - total_purchase_value,
            'selected_year': year,
            'selected_season': season,
    #         'available_seasons': get_available_seasons(),
        })
        return context

#
# User models CRUD
class UserListView(ListView):
    model = User
    template_name = 'mainapp/user_list.html'
    context_object_name = 'users'


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'mainapp/user_profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        print("Profile : ", profile)
        return profile


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'mainapp/user_profile_form.html'

    def get_object(self):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        return reverse_lazy('user-profile')


# class UserProfileAdminEditView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = UserProfileForm
#     template_name = 'mainapp/user_profile_form.html'
#     success_url = reverse_lazy('user-list')
#
#
# class OwnerProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = OwnerProfile
#     form_class = OwnerProfileForm
#     template_name = 'mainapp/owner_profile_form.html'
#
#     def get_object(self):
#         # You can refine this logic if you allow selecting which buyer's owner to edit
#         return OwnerProfile.objects.filter(buyer__created_by=self.request.user).first()
