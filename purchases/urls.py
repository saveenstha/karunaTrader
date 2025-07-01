from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'purchases'

urlpatterns = [

    # Purchase URLs
    path('purchases/', PurchaseBillListView.as_view(), name='purchasebill-list'),
    path('purchases/add/', PurchaseBillCreateView.as_view(), name='purchasebill-add'),
    path('purchases/edit/<int:pk>/', PurchaseBillUpdateView.as_view(), name='purchasebill-edit'),
    path('purchases/delete/<int:pk>/', PurchaseBillDeleteView.as_view(), name='purchasebill-delete'),
]