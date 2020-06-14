from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Poker Players').exists():
            return render(request, "build/index.html")
        else:
            return render(request, 'registration/request_access.html')
    else:
        return redirect('/accounts/login/')
