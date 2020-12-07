from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact Us")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
    else:
        form = UserCreationForm()
        context = {
            "regForm": form
        }
        return render(request, "register.html", context)
    return render(request, "register.html", context)