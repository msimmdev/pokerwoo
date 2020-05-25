from rest_framework.serializers import HyperlinkedModelSerializer
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

class GameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'url',
            'game_number',
            'date_played',
            'stake',
            'place_two_multiplier',
            'place_three_multiplier',
        ]

class GameParticipantSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
    }
    class Meta:
        model = GameParticipant
        fields = ['id', 'url', 'player_ref', 'game', 'place']

class TableSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
    }
    class Meta:
        model = Table
        fields = ['id', 'url', 'level', 'designation', 'starting_chips']

class TableParticipantSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
    }
    class Meta:
        model = TableParticipant
        fields = ['id', 'url', 'game_participant', 'table', 'success']

class RoundSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
    }
    class Meta:
        model = Round
        fields = [
            'id',
            'url',
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

class HandSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
        'round_pk' : 'round__pk',
    }
    class Meta:
        model = Hand
        fields = ['id', 'url', 'table_participant', 'round', 'card1', 'card2']

class RoundWinnerSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'game_pk' : 'game__pk',
        'table_pk' : 'table__pk',
        'round_pk' : 'round__pk',
    }
    class Meta:
        model = RoundWinner
        fields = ['id', 'url', 'table_participant', 'round', 'chips_won']
