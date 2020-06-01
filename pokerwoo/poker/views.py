from rest_framework import viewsets, permissions
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner
from poker.serializers import GameSerializer, GameParticipantSerializer, TableSerializer, TableParticipantSerializer, RoundSerializer, HandSerializer, RoundWinnerSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]

class GameParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = GameParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GameParticipant.objects.filter(game=self.kwargs['game_pk'])

class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Table.objects.filter(game=self.kwargs['game_pk'])

class TableParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = TableParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TableParticipant.objects.filter(table=self.kwargs['table_pk'])

class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Round.objects.filter(table=self.kwargs['table_pk'])

class HandViewSet(viewsets.ModelViewSet):
    serializer_class = HandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Hand.objects.filter(round=self.kwargs['round_pk'])

class RoundWinnerViewSet(viewsets.ModelViewSet):
    serializer_class = RoundWinnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RoundWinner.objects.filter(round=self.kwargs['round_pk'])
