from django.urls import path, include
from rest_framework import routers
from players import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'payment_obligation', views.PaymentObligationViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
