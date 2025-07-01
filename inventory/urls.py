from django.contrib import admin
from django.urls import path, include
from .views import ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView, DailyRateListView, \
    DailyRateCreateView, DailyRateUpdateView, DailyRateDeleteView, RateCalendarView
from datetime import date

app_name = 'inventory'

urlpatterns = [

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/add/', ProductCreateView.as_view(), name='product-add'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product-edit'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),

    path('dailyrates/', DailyRateListView.as_view(), name='dailyrate-list'),
    path('dailyrates/add/', DailyRateCreateView.as_view(), name='dailyrate-add'),
    path('dailyrates/edit/<int:pk>/', DailyRateUpdateView.as_view(), name='dailyrate-edit'),
    path('dailyrates/delete/<int:pk>/', DailyRateDeleteView.as_view(), name='dailyrate-delete'),

    path('calendar/', RateCalendarView.as_view(), name='rate-calendar'),

]