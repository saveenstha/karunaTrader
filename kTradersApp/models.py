from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse


# Create your models here.
class Buyer(models.Model):
    company_name = models.CharField(max_length=255)
    pan_num = models.CharField(max_length=9, primary_key=True, validators=[RegexValidator(r'^\d{1,10}$')])
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now)
    Balance = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('buyer-list')


class OwnerDetails(models.Model):
    pan_num = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact = models.BigIntegerField(blank=True,null=True)
    mobile = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.pan_num)






