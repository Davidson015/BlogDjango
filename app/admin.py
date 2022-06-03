from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = [
    'slug',
    "title",
    "content",
    "image",
    "category",
    "created_at",
    "author",
  ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = [
    'slug',
    "name",
  ]
