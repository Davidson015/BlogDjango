from .models import *

def blog_renderer(request):
  categories = Category.objects.all()
  side_recent_posts = Blog.objects.all().order_by('-created_at')[7:11]
  side_popular_posts = Blog.objects.all().order_by('-created_at')[12:17]

  return {
    'categories': categories,
    'side_recent_posts': side_recent_posts,
    'side_popular_posts': side_popular_posts,
  }