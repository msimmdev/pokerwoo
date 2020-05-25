from rest_framework import serializers
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'game_number',
            'date_played',
            'stake',
            'place_two_multiplier',
            'place_three_multiplier',
        ]

class GameParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameParticipant
        fields = ['id', 'player_ref', 'game', 'place']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'level', 'designation', 'starting_chips']

class TableParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableParticipant
        fields = ['id', 'game_participant', 'table', 'success']

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = [
            'id',
            'table',
            'round_number',
            'big_blind',
            'small_blind',
            'blind_amount',
            'flop1',
            'flop2',
            'flop3',
            'turn',
            'river',
        ]

class HandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hand
        fields = ['id', 'table_participant', 'round', 'card1', 'card2']

class RoundWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundWinner
        fields = ['id', 'table_participant', 'round', 'chips_won']
