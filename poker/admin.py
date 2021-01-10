from django.contrib import admin
from . import models

# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_played', 'game_number']


class GameParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'player_ref', 'game_str']

    def game_str(self, instance):
        return str(instance.game.id) + " " + instance.game.date_played.strftime("%m/%d/%Y") + " " + str(instance.game.game_number)


class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'designation', 'game_str']

    def game_str(self, instance):
        return str(instance.game.id) + " " + instance.game.date_played.strftime("%m/%d/%Y") + " " + str(instance.game.game_number)


class TableParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_participant', 'game_str', 'table_str']

    def game_str(self, instance):
        return str(instance.game.id) + " " + instance.game.date_played.strftime("%m/%d/%Y") + " " + str(instance.game.game_number)

    def table_str(self, instance):
        return str(instance.table.id) + " " + instance.table.designation


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']


class CompetitionGameAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_str', 'competition_str']

    def game_str(self, instance):
        return str(instance.game.id) + " " + instance.game.date_played.strftime("%m/%d/%Y") + " " + str(instance.game.game_number)

    def competition_str(self, instance):
        return instance.competition.name


admin.site.register(models.Game, GameAdmin)
admin.site.register(models.GameParticipant, GameParticipantAdmin)
admin.site.register(models.Table, TableAdmin)
admin.site.register(models.TableParticipant, TableParticipantAdmin)
admin.site.register(models.Competition, CompetitionAdmin)
admin.site.register(models.CompetitionGame, CompetitionGameAdmin)
