from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from signup import forms
from players.models import Player

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data.get('player_id'):
                player = Player.objects.get(pk=form.cleaned_data.get('player_id'))
                player.user = user
                player.save()
            else:
                player = Player(user=user, name=form.cleaned_data.get('player_name'))
                player.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = forms.SignupForm()
    return render(request, 'registration/signup.html', {'form': form})
    