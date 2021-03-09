from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request=request, template_name="login.html")


@login_required(login_url='/login')
def home(request):
    return render(request=request, template_name="home.html")


def logout(request):
    auth_logout(request)
    return redirect('/login')
