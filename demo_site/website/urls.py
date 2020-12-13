from django.urls import path, include
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.index),
    # localhost:8000/services/
    path('services/', views.services),
    # localhost:8000/services/id
    path('services/<int:service_id>', views.single),
    # localhost:8000/blog/
    path('blog/', views.blog)
]