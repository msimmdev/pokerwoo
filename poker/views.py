from rest_framework import viewsets, permissions, views, response, status
from poker.models import Game, GameParticipant, Table, TableParticipant, Round, Hand, RoundWinner
from poker.serializers import GameSerializer, GameParticipantSerializer, TableSerializer, TableParticipantSerializer, RoundSerializer, HandSerializer, RoundWinnerSerializer
import sys

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['date_played']

class PlayerGames(views.APIView):
    def get(self, request):
        games = []
        if 'player_ref' in request.query_params:
            participants = GameParticipant.objects.filter(player_ref=request.query_params['player_ref'])
            for participant in participants:
                games.append(participant.game)
        serializer = GameSerializer(games, many=True, context={'request': request})
        return response.Response(serializer.data)

class GameParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = GameParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GameParticipant.objects.filter(game=self.kwargs['game_pk'])

    def perform_create(self, serializer):
        serializer.save(game=Game.objects.get(pk=self.kwargs['game_pk']))

class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Table.objects.filter(game=self.kwargs['game_pk'])

    def perform_create(self, serializer):
        serializer.save(game=Game.objects.get(pk=self.kwargs['game_pk']))

class TableParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = TableParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TableParticipant.objects.filter(table=self.kwargs['table_pk'], game=self.kwargs['game_pk'])

    def perform_create(self, serializer):
        serializer.save(
            game=Game.objects.get(pk=self.kwargs['game_pk']),
            table=Table.objects.get(pk=self.kwargs['table_pk']),
        )

class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Round.objects.filter(table=self.kwargs['table_pk'], game=self.kwargs['table_pk'])

    def perform_create(self, serializer):
        serializer.save(
            game=Game.objects.get(pk=self.kwargs['game_pk']),
            table=Table.objects.get(pk=self.kwargs['table_pk']),
        )

class HandViewSet(viewsets.ModelViewSet):
    serializer_class = HandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Hand.objects.filter(round=self.kwargs['round_pk'], table=self.kwargs['table_pk'], game=self.kwargs['table_pk'])
        
    def perform_create(self, serializer):
        serializer.save(
            game=Game.objects.get(pk=self.kwargs['game_pk']),
            table=Table.objects.get(pk=self.kwargs['table_pk']),
            round=Round.objects.get(pk=self.kwargs['round_pk']),
        )

class RoundWinnerViewSet(viewsets.ModelViewSet):
    serializer_class = RoundWinnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RoundWinner.objects.filter(round=self.kwargs['round_pk'], table=self.kwargs['table_pk'], game=self.kwargs['table_pk'])

    def perform_create(self, serializer):
        serializer.save(
            game=Game.objects.get(pk=self.kwargs['game_pk']),
            table=Table.objects.get(pk=self.kwargs['table_pk']),
            round=Round.objects.get(pk=self.kwargs['round_pk']),
        )