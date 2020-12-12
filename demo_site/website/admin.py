from django.contrib import admin
from .models import Author, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'published')
    search_fields = ['title', 'author__first_name', 'author__last_name', 'date_created']


admin.site.register(Author)
admin.site.register(Blog, BlogAdmin)