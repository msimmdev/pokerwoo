from django.db import models

# Create your models here.

class Game(models.Model):
    game_number = models.PositiveIntegerField(default=1)
    date_played = models.DateField()
    stake = models.PositiveIntegerField(default=0)
    place_two_multiplier = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    place_three_multiplier = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    complete = models.BooleanField(default=False, blank=True)
    scorable = models.BooleanField(default=True, blank=True)

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

class Competition(models.Model):
    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=False, blank=True)

class CompetitionParticipant(models.Model):
    player_ref = models.PositiveIntegerField(default=0)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='participants')

class CompetitionGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='competitions')
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

class Stats(models.Model):
    player_ref = models.PositiveIntegerField(default=0)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, default=1)
    games_played = models.PositiveIntegerField(default=0)
    games_won = models.PositiveIntegerField(default=0)
    times_placed = models.PositiveIntegerField(default=0)
    place_1 = models.PositiveIntegerField(default=0)
    place_2 = models.PositiveIntegerField(default=0)
    place_3 = models.PositiveIntegerField(default=0)
    net_winnings = models.IntegerField(default=0)
    average_placing = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    average_rating = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    win_rate = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    gain_per_game = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    place_rate = models.DecimalField(default=0, decimal_places=5, max_digits=10)
    score = models.PositiveIntegerField(default=0)