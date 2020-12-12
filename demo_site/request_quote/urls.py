from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/quote
    path('', views.main),
    # localhost:8000/quote/thankyou
    path('thankyou/', views.thankyou),
    
]