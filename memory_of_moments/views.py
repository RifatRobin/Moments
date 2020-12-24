from django.shortcuts import render
from django.contrib.auth.models import auth, User
# Create your views here.


def login(request):
    return render(request, "/login.html")


def register(request):
    return render(request, "/register.html")


def add(request):
    return render(request, "/add_memory.html")


def home(request):
    return render(request, "/view_memory.html")


def delete(request):
    return render(request, "/delete_memory.html")
