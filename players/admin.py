from django.contrib import admin
from . import models

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class PaymentObligationAdmin(admin.ModelAdmin):
    list_display = ['id', 'payer_name', 'payee_name', 'game_ref']

    def payer_name(self, instance):
        return instance.payer.name

    def payee_name(self, instance):
        return instance.payee.name

admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.PaymentObligation, PaymentObligationAdmin)