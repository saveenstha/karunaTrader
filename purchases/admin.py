from django.contrib import admin
from .models import PurchaseBill, PurchaseItem

# Register your models here.
admin.site.register(PurchaseItem)

@admin.register(PurchaseBill)
class PurchaseBillAdmin(admin.ModelAdmin):
    list_display = ['purchase_bill_number', 'farmer', 'date']
    search_fields = ['purchase_bill_number']