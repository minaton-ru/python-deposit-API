from statistics import mode
from django.db import models

class Deposit(models.Model):
    def deposit_default():
        return {}
    date = models.TextField(default='') # начальная дата для вклада, формат dd.mm.YYYY через точку
    periods = models.SmallIntegerField(default=0) # количество месяцев по вкладу
    amount = models.IntegerField(default=0) # сумма вклада
    rate = models.FloatField(default=0) # процент по вкладу
    deposit = models.JSONField(default=deposit_default) # словарь с суммой депозита на каждый месяц