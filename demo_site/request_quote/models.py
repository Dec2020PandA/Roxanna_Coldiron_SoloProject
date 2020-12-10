from django.db import models
# from django.contrib.auth.models import User

# Generic model class for Service or Product
# Only superusers/admins can add products
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

