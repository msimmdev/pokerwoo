from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from players.models import Player, PaymentObligation

class PlayerSerializer(ModelSerializer):
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

class PaymentObligationSerializer(ModelSerializer):
    class Meta:
        model = PaymentObligation
        fields = [
            'id',
            'payer',
            'payee',
            'game_ref',
            'payment_amount',
            'payment_sent',
            'payment_confirmed',
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']