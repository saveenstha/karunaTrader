from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    name = 'transactions'

    def ready(self):
        from .signals import TransactionSignalHandler