from rest_framework import serializers
from .models import Buyer, Farmer, Product, Purchase, Sale


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
