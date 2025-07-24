from django.db import models
from mainapp.models import TimeStampedModel
from django.core.validators import RegexValidator


# people app models
class Buyer(TimeStampedModel):
    company_name = models.CharField(max_length=255)
    pan_num = models.CharField(
        max_length=9,
        primary_key=True,
        validators=[RegexValidator(r'^\d{1,9}$')]
    )
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.company_name


# Owner Profile (of Buyer company)
class OwnerProfile(models.Model):
    buyer = models.OneToOneField('Buyer', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''} ({self.buyer.company_name})"


# Farmers (suppliers)
class Farmer(TimeStampedModel):
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name