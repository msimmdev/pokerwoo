from rest_framework import viewsets, permissions
from players.models import Player, PaymentObligation
from players.serializers import PlayerSerializer, PaymentObligationSerializer, UserSerializer
from django.contrib.auth.models import User

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentObligationViewSet(viewsets.ModelViewSet):
    queryset = PaymentObligation.objects.all()
    serializer_class = PaymentObligationSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='Poker Players')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]