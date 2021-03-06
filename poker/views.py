from rest_framework import viewsets, permissions, views, response
from . import models, serializers, tasks

class GameViewSet(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['date_played']

    def perform_create(self, serializer):
        game = serializer.save()
        if game.complete:
            for participant in game.participants.all():
                for comp in game.competitions.all():
                    tasks.create_stats(participant.player_ref, comp.competition.id)

    def perform_update(self, serializer):
        serializer.save()
        game = self.get_object()
        if game.complete:
            for participant in game.participants.all():
                for comp in game.competitions.all():
                    tasks.create_stats(participant.player_ref, comp.competition.id)

class PlayerGames(views.APIView):
    def get(self, request):
        games = []
        if 'player_ref' in request.query_params:
            participants = models.GameParticipant.objects.filter(player_ref=request.query_params['player_ref'])
            for participant in participants:
                games.append(participant.game)
        serializer = serializers.GameSerializer(games, many=True, context={'request': request})
        return response.Response(serializer.data)

class GameParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GameParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.GameParticipant.objects.filter(game=self.kwargs['game_pk'])

    def perform_create(self, serializer):
        game = models.Game.objects.get(pk=self.kwargs['game_pk'])
        participant = serializer.save(game=game)
        if game.complete:
            for participant in game.participants.all():
                for comp in game.competitions.all():
                    tasks.create_stats(participant.player_ref, comp.competition.id)

    def perform_update(self, serializer):
        serializer.save()
        participant = self.get_object()
        game = models.Game.objects.get(pk=self.kwargs['game_pk'])
        if game.complete:
            for participant in game.participants.all():
                for comp in game.competitions.all():
                    tasks.create_stats(participant.player_ref, comp.competition.id)
        

class TableViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Table.objects.filter(game=self.kwargs['game_pk'])

    def perform_create(self, serializer):
        serializer.save(game=models.Game.objects.get(pk=self.kwargs['game_pk']))

class TableParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TableParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.TableParticipant.objects.filter(table=self.kwargs['table_pk'], game=self.kwargs['game_pk'])

    def perform_create(self, serializer):
        serializer.save(
            game=models.Game.objects.get(pk=self.kwargs['game_pk']),
            table=models.Table.objects.get(pk=self.kwargs['table_pk']),
        )

class StatsViewSet(viewsets.ModelViewSet):
    queryset = models.Stats.objects.all()
    serializer_class = serializers.StatsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['player_ref', 'competition']

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = models.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['active']

class CompetitionGameViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompetitionGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.CompetitionGame.objects.filter(competition=self.kwargs['competition_pk'])
