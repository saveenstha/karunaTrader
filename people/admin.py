from django.contrib import admin
from .models import Buyer, Farmer, OwnerProfile

# Register your models here.
admin.site.register(Buyer)
admin.site.register(OwnerProfile)
admin.site.register(Farmer)
