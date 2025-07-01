from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'sales'

urlpatterns = [
    # Sale URLs
    path('sales/', SalesBillListView.as_view(), name='salesbill-list'),
    path('sales/add/', SalesBillCreateView.as_view(), name='salesbill-add'),
    path('sales/edit/<int:pk>/', SalesBillUpdateView.as_view(), name='salesbill-edit'),
    path('sales/delete/<int:pk>/', SalesBillDeleteView.as_view(), name='salesbill-delete'),
]