from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import Author, Blog, Comment
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
        'all_blogs': Blog.objects.all(),
    }
    return render(request, "blogs.html", context)

def single_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog' : blog,
    }
    return render(request, "single_blog.html", context)

def new_comment(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    Comment.objects.create(content=request.POST['comment'], poster=request.user, blog_post=blog)
    return redirect(single_blog, blog_id=blog.id)


def add_likes(request, blog_id):
    liked_blog = Blog.objects.get(id=blog_id)
    user_liking = request.user
    liked_blog.user_likes.add(user_liking)
    return redirect(single_blog, blog_id=liked_blog.id)

