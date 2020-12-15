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
    path('blog/', views.blog),
    # localhost:8000/blog/id
    path("blog/<int:blog_id>", views.single_blog),
    # blog comments
    path('blog/<int:blog_id>/new_comment/', views.new_comment),
    # add likes
    path('add_like/<int:blog_id>', views.add_likes)
]