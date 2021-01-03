from django.urls import path, include
from . import views
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

router = SimpleRouter()
router.register(r'games', views.GameViewSet)
router.register(r'stats', views.StatsViewSet)
router.register(r'competitions', views.CompetitionViewSet)

competition_router = NestedSimpleRouter(router, r'competitions', lookup='competition')
competition_router.register(r'games', views.CompetitionGameViewSet, basename='competitiongame')

game_router = NestedSimpleRouter(router, r'games', lookup='game')
game_router.register(r'participants', views.GameParticipantViewSet, basename='gameparticipant')
game_router.register(r'tables', views.TableViewSet, basename='table')

table_router = NestedSimpleRouter(game_router, r'tables', lookup='table')
table_router.register(r'participants', views.TableParticipantViewSet, basename='tableparticipant')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(game_router.urls)),
    path('', include(table_router.urls)),
    path('', include(competition_router.urls)),
    path('player_games/', views.PlayerGames.as_view()),
]
