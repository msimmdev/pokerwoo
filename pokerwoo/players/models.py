from django.db import models

# Create your models here.

class Player(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    pokerth_name = models.CharField(max_length=255)
    avatar = models.URLField(blank=True)
    payment_link = models.URLField(blank=True)
    payment_name = models.CharField(max_length=255, blank=True)
    bank_account_number = models.CharField(max_length=30, blank=True)
    bank_sort_code = models.CharField(max_length=6, blank=True)
    active = models.BooleanField()

class PaymentObligation(models.Model):
    payer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    payee = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    game_ref = models.PositiveIntegerField(default=0)
    payment_amount = models.PositiveIntegerField(default=0)

