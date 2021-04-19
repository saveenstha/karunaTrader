from django.contrib import admin
from .models import Buyer, Transaction, ParticularsDetail

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Transaction)
admin.site.register(ParticularsDetail)