from django.db import models

# Create your models here.

class Session(models.Model):
    schedule_date = models.DateTimeField()
    createdby_player = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)

class SessionPlayer(models.Model):
    player_ref = models.PositiveIntegerField(default=0)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='players')
    attendance = models.BooleanField(null=True)
