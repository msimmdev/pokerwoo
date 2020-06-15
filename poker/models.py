from django.db import models

# Create your models here.

class Game(models.Model):
    game_number = models.PositiveIntegerField(default=1)
    date_played = models.DateField()
    stake = models.PositiveIntegerField(default=0)
    place_two_multiplier = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    place_three_multiplier = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    complete = models.BooleanField(default=False, blank=True)

class GameParticipant(models.Model):
    player_ref = models.PositiveIntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='participants')
    place = models.PositiveIntegerField(default=0, blank=True)

class Table(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='tables')
    level = models.PositiveIntegerField(default=0, blank=True)
    designation = models.CharField(max_length = 10)
    starting_chips = models.PositiveIntegerField(default=0, null=True, blank=True)
    progressing = models.PositiveIntegerField(default=0, blank=True)

class TableParticipant(models.Model):
    game_participant = models.ForeignKey(GameParticipant, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='participants')
    success = models.BooleanField(default=False, blank=True)

class Round(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    round_number = models.PositiveIntegerField(default=1)
    big_blind = models.ForeignKey(TableParticipant, null=True, on_delete=models.SET_NULL, related_name='+')
    small_blind = models.ForeignKey(TableParticipant, null=True, on_delete=models.SET_NULL, related_name='+')
    blind_amount = models.PositiveIntegerField(default=0)
    flop1 = models.PositiveIntegerField(default=0)
    flop3 = models.PositiveIntegerField(default=0)
    flop2 = models.PositiveIntegerField(default=0)
    turn = models.PositiveIntegerField(default=0)
    river = models.PositiveIntegerField(default=0)

class Hand(models.Model):
    table_participant = models.ForeignKey(TableParticipant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    card1 = models.PositiveIntegerField(default=0)
    card2 = models.PositiveIntegerField(default=0)

class RoundWinner(models.Model):
    table_participant = models.ForeignKey(TableParticipant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    chips_won = models.PositiveIntegerField(default=0)
