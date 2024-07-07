import logging
from .models import Transactions
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

logger = logging.getLogger(__name__)


class TransactionSignalHandler:

    @staticmethod
    @receiver(post_save, sender=Transaction)
    def update_buyer_balance_on_save(sender, instance, created, **kwargs):
        buyer = instance.buyer
        if created:
            if instance.transaction_type == 'credit':
                buyer.balance += instance.amount
            elif instance.transaction_type == 'debit':
                buyer.balance -= instance.amount
            buyer.save()
        else:
            old_transaction = Transaction.objects.get(pk=instance.pk)
            if old_transaction.transaction_type == 'credit':
                buyer.balance -= old_transaction.amount
            elif old_transaction.transaction_type == 'debit':
                buyer.balance += old_transaction.amount

            if instance.transaction_type == 'credit':
                buyer.balance += instance.amount
            elif instance.transaction_type == 'debit':
                buyer.balance -= instance.amount
            buyer.save()

        logger.info(f"Updated buyer balance to {buyer.balance} for transaction {instance}")


    @staticmethod
    @receiver(pre_delete, sender=Transaction)
    def update_buyer_balance_on_delete(sender, instance, **kwargs):
        buyer = instance.buyer
        if instance.transaction_type == 'credit':
            buyer.balance -= instance.amount
        elif instance.transaction_type == 'debit':
            buyer.balance += instance.amount
        buyer.save()

        logger.info(f"Updated buyer balance to {buyer.balance} after deleting transaction {instance}")
