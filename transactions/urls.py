from django.urls import path
from .views import (
    AddTransactionView, DeleteTransactionViews #, AddParticularsView
)

urlpatterns = [
    path('transactions/add/', AddTransactionView.as_view(), name='add-transaction'),
    path('transactions/<int:pk>/delete/', DeleteTransactionViews.as_view(), name='delete-transaction'),

]