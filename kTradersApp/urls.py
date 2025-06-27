from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import models, views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from .views_old import *
from . import *


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    # path('Dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('buyer/all/', AllBuyersView.as_view(), name='all-buyer'),
    # path('buyer/add/', BuyerCreateView.as_view(), name='add-buyer'),
    path ('buyers_list/', BuyerListView.as_view (), name='buyer-list'),
    path('buyer/edit/<str:pk>', BuyerUpdateView.as_view(), name='edit-buyer'),
    path('buyer/<int:pk>/delete', BuyerDeleteView.as_view(), name='delete-buyer'),
    path ('buyer/<int:pk>/profile/', BuyerProfileDetailView.as_view(), name='buyer-profile'),
    path('buyer/edit-profile/<str:pk>', BuyerProfileUpdateView.as_view(), name='edit-owner-info'),
    # path ('buyer/add_transaction', views.AddTransactionView, name='add-transaction'),
    # path ('buyer/add_details/', AddParticularsView.as_view(), name='add-particulars'),

    # New Refined models urls

    path('buyers/', views.BuyerListView.as_view(), name='buyer-list'),
    path('buyers/add/', views.BuyerCreateView.as_view(), name='buyer-add'),
    path('buyers/edit/<str:pk>/', views.BuyerUpdateView.as_view(), name='buyer-edit'),
    path('buyers/delete/<str:pk>/', views.BuyerDeleteView.as_view(), name='buyer-delete'),

    path('ownerdetails/', views.OwnerDetailsListView.as_view(), name='ownerdetails-list'),
    path('ownerdetails/add/', views.OwnerDetailsCreateView.as_view(), name='ownerdetails-add'),
    path('ownerdetails/edit/<str:pk>/', views.OwnerDetailsUpdateView.as_view(), name='ownerdetails-edit'),
    path('ownerdetails/delete/<str:pk>/', views.OwnerDetailsDeleteView.as_view(), name='ownerdetails-delete'),

    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product-add'),

    # Farmer URLs
    path('farmers/', views.FarmerListView.as_view(), name='farmer-list'),
    path('farmers/add/', views.FarmerCreateView.as_view(), name='farmer-add'),
    path('farmers/edit/<int:pk>/', views.FarmerUpdateView.as_view(), name='farmer-edit'),
    path('farmers/delete/<int:pk>/', views.FarmerDeleteView.as_view(), name='farmer-delete'),

    # Purchase URLs
    path('purchases/', views.PurchaseListView.as_view(), name='purchase-list'),
    path('purchases/add/', views.PurchaseCreateView.as_view(), name='purchase-add'),
    path('purchases/edit/<int:pk>/', views.PurchaseUpdateView.as_view(), name='purchase-edit'),
    path('purchases/delete/<int:pk>/', views.PurchaseDeleteView.as_view(), name='purchase-delete'),

    # Sale URLs
    path('sales/', views.SaleListView.as_view(), name='sale-list'),
    path('sales/add/', views.SaleCreateView.as_view(), name='sale-add'),
    path('sales/edit/<int:pk>/', views.SaleUpdateView.as_view(), name='sale-edit'),
    path('sales/delete/<int:pk>/', views.SaleDeleteView.as_view(), name='sale-delete'),

]
