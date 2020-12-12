from django.urls import path, include
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index),
    # localhost:8000/about/
    path('about/', views.about),
    # localhost:8000/services/
    path('services/', views.services),
    # localhost:8000/contact/
    path('contact/', views.contact), 
]