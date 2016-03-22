from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
    account_name = models.CharField(max_length=20)
    account_id = models.IntegerField(primary_key=True)
    balance = models.DecimalField(max_digits=2, decimal_places=2)