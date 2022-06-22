from unicodedata import category
from .models import *

def blog_renderer(request):
  categories = Category.objects.all()
  counts = []
  side_recent_posts = Blog.objects.all().order_by('-created_at')[7:11]
  side_popular_posts = Blog.objects.all().order_by('-created_at')[12:17]

  for c in categories:
    count = Blog.objects.filter(category=c).count()
    counts.append(count)

  categories_counts = zip(categories, counts)

  return {
    'categories': categories,
    'categories_counts': categories_counts,
    'side_recent_posts': side_recent_posts,
    'side_popular_posts': side_popular_posts,
  }