from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from poker.models import Game, GameParticipant, Table, TableParticipant, Stats, Competition, CompetitionParticipant, CompetitionGame

class CompetitionParticipantSerializer(ModelSerializer):
    class Meta:
        model = CompetitionParticipant
        fields = [
            'player_ref',
        ]

class CompetitionGameSerializer(ModelSerializer):
    class Meta:
        model = CompetitionGame
        fields = [
            'id',
            'game',
            'competition',
        ]

class CompetitionSerializer(ModelSerializer):
    participants = CompetitionParticipantSerializer(read_only=True, many=True)
    class Meta:
        model = Competition
        fields = [
            'id',
            'name',
            'order',
            'active',
            'participants',
        ]

class GameParticipantSerializer(ModelSerializer):
    game = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = GameParticipant
        fields = ['id', 'player_ref', 'game', 'place']

class GameSerializer(ModelSerializer):
    participants = GameParticipantSerializer(read_only=True, many=True)
    tables = PrimaryKeyRelatedField(read_only=True, many=True)
    competitions = CompetitionGameSerializer(read_only=True, many=True)
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
            'competitions',
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

class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = [
            'id',
            'player_ref',
            'games_played',
            'games_won',
            'times_placed',
            'place_1',
            'place_2',
            'place_3',
            'net_winnings',
            'average_placing',
            'average_rating',
            'win_rate',
            'place_rate',
            'gain_per_game',
            'score',
            'new_score',
            'competition',
        ]

