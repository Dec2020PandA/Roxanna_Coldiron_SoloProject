from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from request_quote.models import Item


def index(request):
    context = {
        'services': Item.objects.all()
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    context = {
        'services': Item.objects.all()
    }
    return render(request, "services.html", context)

def contact(request):
    return render(request, "contact.html")