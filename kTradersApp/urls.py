from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import models, views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    # path('Dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', login_required(Dashboard.as_view()), name='dashboard'),
    path('buyer/all/', AllBuyersView.as_view(), name='all-buyer'),
    path('buyer/add/', BuyerCreateView.as_view(), name='add-buyer'),
    path ('buyers_list/', BuyerListView.as_view (), name='buyer-list'),
    path('buyer/edit/<str:pk>', BuyerUpdateView.as_view(), name='edit-buyer'),
    path('buyer/<int:pk>/delete', BuyerDeleteView.as_view(), name='delete-buyer'),
    path ('buyer/<int:pk>/profile/', BuyerProfileDetailView.as_view(), name='buyer-profile'),
    path('buyer/edit-profile/<str:pk>', BuyerProfileUpdateView.as_view(), name='edit-owner-info'),
    # path ('buyer/add_transaction', views.AddTransactionView, name='add-transaction'),
    # path ('buyer/add_details/', AddParticularsView.as_view(), name='add-particulars'),
]
