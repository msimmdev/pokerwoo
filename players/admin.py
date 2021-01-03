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

class AwardAdmin(admin.ModelAdmin):
    list_display = ['id','player_name','name','award_key']

    def player_name(self, instance):
        return instance.player.name

admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.PaymentObligation, PaymentObligationAdmin)
admin.site.register(models.Award, AwardAdmin)
