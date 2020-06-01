from rest_framework.serializers import ModelSerializer
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner

class GameSerializer(ModelSerializer):
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

class GameParticipantSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
    }
    class Meta:
        model = GameParticipant
        fields = ['id', 'player_ref', 'game', 'place']

class TableSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
    }
    class Meta:
        model = Table
        fields = ['id', 'level', 'designation', 'game', 'starting_chips']

class TableParticipantSerializer(ModelSerializer):
    class Meta:
        model = TableParticipant
        fields = ['id', 'game_participant', 'table', 'game', 'success']

class RoundSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
    }
    class Meta:
        model = Round
        fields = [
            'id',
            'table',
            'game',
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

class HandSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
        'round_pk' : 'round__pk',
    }
    class Meta:
        model = Hand
        fields = ['id', 'table_participant', 'round', 'table', 'game', 'card1', 'card2']

class RoundWinnerSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
        'round_pk' : 'round__pk',
    }
    class Meta:
        model = RoundWinner
        fields = ['id', 'table_participant', 'round', 'table', 'game', 'chips_won']
