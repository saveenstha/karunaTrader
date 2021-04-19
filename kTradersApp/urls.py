from django.contrib import admin

from django.urls import path
from . import models, views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    BuyerCreateView, BuyerListView, BuyerUpdateView, BuyerDeleteView, AllBuyersView, BuyerProfileDetailView,
    AddTransactionView,
)

urlpatterns = [
    path('', views.starter, name='starter'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('Dashboard/', views.dashboard, name='dashboard'),
    path('buyer/all/', AllBuyersView.as_view(), name='all-buyer'),
    path('buyer/add/', BuyerCreateView.as_view(), name='add-buyer'),
    path ('buyers_list/', BuyerListView.as_view (), name='buyer-list'),
    path('buyer/edit/<str:pk>', BuyerUpdateView.as_view(), name='edit-buyer'),
    path('buyer/<int:pk>/delete', BuyerDeleteView.as_view(), name='delete-buyer'),
    path ('buyer/<int:pk>/profile/', BuyerProfileDetailView.as_view(), name='buyer-profile'),
    path ('buyer/transaction/add', views.AddParticulars, name='add-transaction'),
]
