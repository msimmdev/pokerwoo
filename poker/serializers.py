from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner

class GameParticipantSerializer(ModelSerializer):
    game = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = GameParticipant
        fields = ['id', 'player_ref', 'game', 'place']

class GameSerializer(ModelSerializer):
    participants = GameParticipantSerializer(read_only=True, many=True)
    tables = PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Game
        fields = [
            'id',
            'game_number',
            'date_played',
            'stake',
            'place_two_multiplier',
            'place_three_multiplier',
            'complete',
            'participants',
            'tables',
        ]

class TableParticipantSerializer(ModelSerializer):
    table = PrimaryKeyRelatedField(read_only=True)
    game = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = TableParticipant
        fields = ['id', 'game_participant', 'table', 'game', 'success']

class TableSerializer(ModelSerializer):
    participants = TableParticipantSerializer(read_only=True, many=True)
    game = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Table
        fields = ['id', 'level', 'designation', 'game', 'progressing', 'starting_chips', 'participants']

class RoundSerializer(ModelSerializer):
    table = PrimaryKeyRelatedField(read_only=True)
    game = PrimaryKeyRelatedField(read_only=True)
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
    round = PrimaryKeyRelatedField(read_only=True)
    table = PrimaryKeyRelatedField(read_only=True)
    game = PrimaryKeyRelatedField(read_only=True)
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
        'round_pk' : 'round__pk',
    }
    class Meta:
        model = Hand
        fields = ['id', 'table_participant', 'round', 'table', 'game', 'card1', 'card2']

class RoundWinnerSerializer(ModelSerializer):
    round = PrimaryKeyRelatedField(read_only=True)
    table = PrimaryKeyRelatedField(read_only=True)
    game = PrimaryKeyRelatedField(read_only=True)
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
        'round_pk' : 'round__pk',
    }
    class Meta:
        model = RoundWinner
        fields = ['id', 'table_participant', 'round', 'table', 'game', 'chips_won']
