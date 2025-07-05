from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'purchases'

urlpatterns = [

    # Purchase URLs
    path('', PurchaseBillListView.as_view(), name='purchasebill-list'),
    path('add/', PurchaseBillCreateView.as_view(), name='purchasebill-add'),
    path('edit/<int:pk>/', PurchaseBillUpdateView.as_view(), name='purchasebill-edit'),
    path('delete/<int:pk>/', PurchaseBillDeleteView.as_view(), name='purchasebill-delete'),

    path('purchaseitem/add/<int:bill_id>/', PurchaseItemCreateView.as_view(), name='purchaseitem-add'),
    path('item/<int:pk>/edit/', PurchaseItemEditView.as_view(), name='purchaseitem-edit'),
    path('item/<int:pk>/delete/', PurchaseItemDeleteView.as_view(), name='purchaseitem-delete'),

]