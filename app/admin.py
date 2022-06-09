from django.contrib import admin
from app.models import *
from import_export.admin import ImportExportMixin

# Register your models here.

# Exporting Blogs to CSV
class BlogAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display = [
    "title",
    "content",
    "category",
    "created_at",
    "author",
  ]
admin.site.register(Blog, BlogAdmin)

# Exporting Categories to CSV
class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
  list_display = [
    "name",
  ]
admin.site.register(Category, CategoryAdmin)
