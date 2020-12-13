from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import Author, Blog
from request_quote.models import Item


def index(request):
    context = {
        'services': Item.objects.all()
    }
    return render(request, "home.html", context)

def services(request):
    context = {
        'services': Item.objects.all()
    }
    return render(request, "services.html", context)

def single(request, service_id):
    service = Item.objects.get(id=service_id)
    context = {
        'service': service
    }
    return render(request, "single_service.html", context)

def blog(request):
    context = {
        'all_blogs': Blog.objects.all()
    }
    return render(request, "blogs.html", context)
