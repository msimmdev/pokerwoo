from rest_framework import viewsets
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner
from poker.serializers import GameSerializer, GameParticipantSerializer, TableSerializer, TableParticipantSerializer, RoundSerializer, HandSerializer, RoundWinnerSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = GameParticipantSerializer

    def get_queryset(self):
        return GameParticipant.objects.filter(game=self.kwargs['game_pk'])

class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer

    def get_queryset(self):
        return Table.objects.filter(game=self.kwargs['game_pk'])

class TableParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = TableParticipantSerializer

    def get_queryset(self):
        return TableParticipant.objects.filter(game=self.kwargs['table_pk'])

class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer

    def get_queryset(self):
        return Round.objects.filter(game=self.kwargs['table_pk'])

class HandViewSet(viewsets.ModelViewSet):
    serializer_class = HandSerializer

    def get_queryset(self):
        return Hand.objects.filter(game=self.kwargs['round_pk'])

class RoundWinnerViewSet(viewsets.ModelViewSet):
    serializer_class = RoundWinnerSerializer

    def get_queryset(self):
        return RoundWinner.objects.filter(game=self.kwargs['round_pk'])