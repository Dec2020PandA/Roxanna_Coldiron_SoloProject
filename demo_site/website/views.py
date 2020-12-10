from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .forms import UserCreateForm


def index(request):
    return render(request, "home.html")

def about(request):
    return HttpResponse("About Us")

def contact(request):
    return HttpResponse("Contact Us")

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # User.objects.create_user(
            #     username=request.POST['username'],
            #     first_name=request.POST['first_name'], 
            #     last_name=request.POST['last_name'],
            #     email=request.POST['email'],
            #     password=request.POST['password1']
            # )
            messages.success(request, 'Account created successfully')
            return redirect("/")

    else:
        form = UserCreateForm()
        context = {
            "regForm": form
        }
        return render(request, "register.html", context)