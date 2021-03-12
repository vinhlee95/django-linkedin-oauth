from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def login(request):
    if request.user.is_authenticated:
        return redirect(to="/home")

    return render(request=request, template_name="login.html")


def home(request):
    return render(request=request, template_name="home.html")


def logout(request):
    auth_logout(request)
    return redirect('/login')
