from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User
from players.models import Player, PaymentObligation

class PlayerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = [
            'id',
            'user',
            'name',
            'pokerth_name',
            'avatar',
            'payment_link',
            'payment_name',
            'bank_account_number',
            'bank_sort_code',
            'active',
        ]

class PaymentObligationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PaymentObligation
        fields = [
            'id',
            'payer',
            'payee',
            'game_ref',
            'payment_amount',
        ]

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']