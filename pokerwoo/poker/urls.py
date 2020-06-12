from django.urls import path, include
from poker.views import GameViewSet, GameParticipantViewSet, TableViewSet, TableParticipantViewSet, RoundViewSet, HandViewSet, RoundWinnerViewSet, PlayerGames
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

router = SimpleRouter()
router.register(r'games', GameViewSet)

game_router = NestedSimpleRouter(router, r'games', lookup='game')
game_router.register(r'participants', GameParticipantViewSet, basename='gameparticipant')
game_router.register(r'tables', TableViewSet, basename='table')

table_router = NestedSimpleRouter(game_router, r'tables', lookup='table')
table_router.register(r'participants', TableParticipantViewSet, basename='tableparticipant')
table_router.register(r'rounds', RoundViewSet, basename='round')

round_router = NestedSimpleRouter(table_router, r'rounds', lookup='round')
round_router.register(r'hands', HandViewSet, basename='hand')
round_router.register(r'winners', RoundWinnerViewSet, basename='roundwinner')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(game_router.urls)),
    path('', include(table_router.urls)),
    path('', include(round_router.urls)),
    path('player_games/', PlayerGames.as_view()),
]
