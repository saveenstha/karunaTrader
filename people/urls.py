from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'people'

urlpatterns = [
    path('buyers/', BuyerListView.as_view(), name='buyer-list'),
    path('buyers/add/', BuyerCreateView.as_view(), name='buyer-add'),
    path('buyers/edit/<str:pk>/', BuyerUpdateView.as_view(), name='buyer-edit'),
    path('buyers/delete/<str:pk>/', BuyerDeleteView.as_view(), name='buyer-delete'),
    path('buyers/profile/<str:pk>/', BuyerProfileView.as_view(), name='buyer-profile'),

    path('ownerprofiles/', OwnerProfilesListView.as_view(), name='ownerprofiles-list'),
    path('ownerprofiles/add/', OwnerProfilesCreateView.as_view(), name='ownerprofiles-add'),
    path('ownerprofiles/edit/<str:pk>/', OwnerProfilesUpdateView.as_view(), name='ownerprofiles-edit'),
    path('ownerprofiles/delete/<str:pk>/', OwnerProfilesDeleteView.as_view(), name='ownerprofiles-delete'),

    # Farmer URLs
    path('farmers/', FarmerListView.as_view(), name='farmer-list'),
    path('farmers/add/', FarmerCreateView.as_view(), name='farmer-add'),
    path('farmers/edit/<int:pk>/', FarmerUpdateView.as_view(), name='farmer-edit'),
    path('farmers/delete/<int:pk>/', FarmerDeleteView.as_view(), name='farmer-delete'),
    path('farmers/profile/<int:pk>/', FarmerProfileView.as_view(), name='farmer-profile'),
]