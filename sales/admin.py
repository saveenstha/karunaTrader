from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SalesItem)

@admin.register(SalesBill)
class SalesBillAdmin(admin.ModelAdmin):
    list_display = ['sales_bill_number', 'buyer', 'date']
    search_fields = ['sales_bill_number']