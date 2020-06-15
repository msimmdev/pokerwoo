from django.db import models

# Create your models here.

class Player(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    pokerth_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    payment_link = models.URLField(blank=True, null=True)
    payment_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=30, blank=True, null=True)
    bank_sort_code = models.CharField(max_length=6, blank=True, null=True)
    active = models.BooleanField(default=True, blank=True)

class PaymentObligation(models.Model):
    payer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    payee = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    game_ref = models.PositiveIntegerField(default=0)
    payment_amount = models.PositiveIntegerField(default=0)
    payment_sent = models.BooleanField(default=False, blank=True)
    payment_confirmed = models.BooleanField(default=False, blank=True)
    