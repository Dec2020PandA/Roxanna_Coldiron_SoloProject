from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


# Blogs will be added to admin. Only staff/superusers can post.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    featured_image = models.ImageField(blank=True)
    body = RichTextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    published = models.BooleanField(default=False)
    user_likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)

    def __str__(self):
        return self.title


# Blog comments and replies
class Comment(models.Model):
    content = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    blog_post = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)


