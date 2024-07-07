import sys
print(sys.path) # Debug print to check the Python path

from django.test import TestCase
from .models import Buyer, Transaction
from django.contrib.auth.models import User


# Create your tests here.
class SignalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.buyer = Buyer.objects.create(
            company_name='Test Company',
            pan_num='123456789',
            created_by=self.user,
            balance=0
        )

    def test_create_transaction(self):
        transaction = Transaction.objects.create(
            buyer = self.buyer,
            transaction_type = 'credit',
            amount = 100
        )
        self.buyer.refresh_from_db()
        self.assertEqual(self.buyer.balance, 100)

    def test_update_transaction(self):
        transaction = Transaction.objects.create(
            buyer=self.buyer,
            transaction_type='credit',
            amount=100
        )
        transaction.amount = 200
        transaction.save()
        self.buyer.refresh_from_db()
        self.assertEqual(self.buyer.balance, 200)

    def test_delete_transaction(self):
        transaction = Transaction.objects.create(
            buyer=self.buyer,
            transaction_type='credit',
            amount=100
        )
        transaction.delete()
        self.buyer.refresh_from_db()
        self.assertEqual(self.buyer.balance, 0)