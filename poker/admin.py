from django.contrib import admin
from . import models

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_played', 'game_number']

class GameParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'player_ref', 'game_str']

    def game_str(self, instance):
        return instance.game.id + " " + instance.game.date_played + " " + instance.game.game_number

class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'designation', 'game_str']

    def game_str(self, instance):
        return instance.game.id + " " + instance.game.date_played + " " + instance.game.game_number

class TableParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_participant', 'game_str', 'table_str']

    def game_str(self, instance):
        return instance.game.id + " " + instance.game.date_played + " " + instance.game.game_number

    def table_str(self, instance):
        return instance.table.id + " " + instance.table.designation

admin.site.register(models.Game, GameAdmin)
admin.site.register(models.GameParticipant, GameParticipantAdmin)
admin.site.register(models.Table, TableAdmin)
admin.site.register(models.TableParticipant, TableParticipantAdmin)