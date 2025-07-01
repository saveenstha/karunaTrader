from django.contrib import admin
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView

from django.contrib.auth.decorators import login_required
from django.urls import path
from . import models, views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import LandingPageView, DashboardView, UserListView, UserProfileDetailView
# from .views_old import *
# from . import *


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # path('buyer/all/', AllBuyersView.as_view(), name='all-buyer'),
    # path('buyer/add/', BuyerCreateView.as_view(), name='add-buyer'),
    # path ('buyers_list/', BuyerListView.as_view (), name='buyer-list'),
    # path('buyer/edit/<str:pk>', BuyerUpdateView.as_view(), name='edit-buyer'),
    # path('buyer/<int:pk>/delete', BuyerDeleteView.as_view(), name='delete-buyer'),
    # path ('buyer/<int:pk>/profile/', BuyerProfileDetailView.as_view(), name='buyer-profile'),
    # path('buyer/edit-profile/<str:pk>', BuyerProfileUpdateView.as_view(), name='edit-owner-info'),
    # path ('buyer/add_transaction', views.AddTransactionView, name='add-transaction'),
    # path ('buyer/add_details/', AddParticularsView.as_view(), name='add-particulars'),

    # # New Refined models urls
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    # path('users/<int:pk>/edit/', UserProfileAdminEditView.as_view(), name='user-profile-edit'),
    #
    #
    # path('profile/', UserProfileUpdateView.as_view(), name='user-profile'),
    # path('owner-profile/', OwnerProfileUpdateView.as_view(), name='owner-profile'),
    #
    #

]
