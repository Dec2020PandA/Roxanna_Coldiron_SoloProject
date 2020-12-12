from django.contrib import admin
from .models import Item

# class ItemsAdmin(admin.ModelAdmin):

admin.site.register(Item)
