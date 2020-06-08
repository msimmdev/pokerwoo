from rest_framework import viewsets, permissions, views, response, status
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
    filterset_fields = ['payer', 'payee']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(groups__name='Poker Players')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActivePlayer(views.APIView):
    def get(self, request):
        players = Player.objects.filter(user=self.request.user.id)
        if len(players) > 0:
            serializer = PlayerSerializer(players[0], context={'request': request})
            return response.Response(serializer.data)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
