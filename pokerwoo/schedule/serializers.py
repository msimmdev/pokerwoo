from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from schedule.models import Session, SessionPlayer

class SessionPlayerSerializer(ModelSerializer):
    session = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SessionPlayer
        fields = [
            'id',
            'player_ref',
            'session',
            'attendance',
        ]

class SessionSerializer(ModelSerializer):
    players = SessionPlayerSerializer(read_only=True, many=True)
    class Meta:
        model = Session
        fields = [
            'id',
            'schedule_date',
            'createdby_player',
            'description',
            'players',
        ]