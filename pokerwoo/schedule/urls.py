from django.urls import path, include
from schedule import views
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter

router = SimpleRouter()
router.register(r'sessions', views.SessionViewSet)

player_router = NestedSimpleRouter(router, r'sessions', lookup='session')
player_router.register(r'players', views.SessionPlayerViewSet, basename='sessionplayer')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(player_router.urls)),
]
