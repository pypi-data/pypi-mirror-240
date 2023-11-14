from django.db import models

from .base import BaseModelAbstract
from ... import constants


class BankAccount(BaseModelAbstract, models.Model):
    account_type = models.CharField(choices=constants.BANK_ACCOUNT_TYPES,
                                    default=constants.CORPORATE_BANK_ACCOUNT)
    currency = models.CharField(max_length=5, default='USD')
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    sort_code = models.CharField(max_length=20)
    third_party_id = models.CharField(null=True, blank=True, editable=False)

    def __unicode__(self):
        return f"{self.bank_name}|{self.account_number}|{self.sort_code}"
