from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "build/index.html")
    else:
        return redirect('/accounts/login/')
