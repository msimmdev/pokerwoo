from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from players import models

class SignupForm(UserCreationForm):
    player_choices = [('', '')]
    # player_set = models.Player.objects.filter(user=None)
    # for player in player_set:
    #     player_choices.append((player.id, player.name))

    email = forms.EmailField(required=True, label='Email')
    player_id = forms.ChoiceField(label='Choose an existing player', choices = player_choices, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    player_name = forms.CharField(label='OR provide a name for a new player', required=False, max_length=100)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data=super().clean()
        if not cleaned_data.get('player_id') and not cleaned_data.get('player_name'):
            self.add_error('player_id', 'You must choose a player or provide a name.')
