from django.urls import path, include
from poker.views import GameViewSet, GameParticipantViewSet, TableViewSet, TableParticipantViewSet, RoundViewSet, HandViewSet, RoundWinnerViewSet
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

router = DefaultRouter()
router.register(r'games', GameViewSet)

game_router = NestedDefaultRouter(router, r'games', lookup='game')
game_router.register(r'participants', GameParticipantViewSet, basename='gameparticipant')
game_router.register(r'tables', TableViewSet, basename='tables')

table_router = NestedDefaultRouter(game_router, r'tables', lookup='table')
table_router.register(r'participants', TableParticipantViewSet, basename='participants')
table_router.register(r'rounds', RoundViewSet, basename='rounds')

round_router = NestedDefaultRouter(table_router, r'rounds', lookup='round')
round_router.register(r'hands', HandViewSet, basename='hands')
round_router.register(r'winners', RoundWinnerViewSet, basename='winners')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(game_router.urls)),
    path('', include(table_router.urls)),
    path('', include(round_router.urls)),
]
