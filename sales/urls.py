from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'sales'

urlpatterns = [
    # Sale URLs
    path('', SalesBillListView.as_view(), name='salesbill-list'),
    path('add/', SalesBillCreateView.as_view(), name='salesbill-add'),
    path('edit/<int:pk>/', SalesBillUpdateView.as_view(), name='salesbill-update'),
    path('delete/<int:pk>/', SalesBillDeleteView.as_view(), name='salesbill-delete'),

    path('item/add/<int:bill_id>/', SalesItemCreateView.as_view(), name='salesitem-add'),
    path('item/<int:pk>/edit/', SalesItemEditView.as_view(), name='salesitem-edit'),
    path('item/<int:pk>/delete/', SalesItemDeleteView.as_view(), name='salesitem-delete'),
]