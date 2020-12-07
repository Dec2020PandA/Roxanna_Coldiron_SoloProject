from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index),
    # localhost:8000/about/
    path('about/', views.about),
    # localhost:8000/contact/
    path('contact/', views.contact), 
    # localhost:8000/register/
    path('register/', views.register), 
]