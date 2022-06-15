from django.shortcuts import get_object_or_404, redirect, render
from app.forms import CommentForm

from app.models import *

# Create your views here.
# Index (Home) Page
def IndexPage(request):
  template_name = 'index.html'
  category = Category.objects.all()
  featured_posts = Blog.objects.all()[:3]
  recent_posts = Blog.objects.all().order_by('-created_at')[3:7]
  side_recent_posts = Blog.objects.all().order_by('-created_at')[7:11]
  popular_post = Blog.objects.all().order_by('-created_at')[11]
  side_popular_posts = Blog.objects.all().order_by('-created_at')[12:17]
  most_read_posts = Blog.objects.all().order_by('-created_at')[17:21]
  hot_post = Blog.objects.all().order_by('?')[0]
  top_of_the_week = Blog.objects.all().order_by('-created_at')[21:24]

  context = {
    'category': category,
    'featured_posts': featured_posts,
    'recent_posts': recent_posts,
    'side_recent_posts': side_recent_posts,
    'popular_post': popular_post,
    'side_popular_posts': side_popular_posts,
    'most_read_posts': most_read_posts,
    'hot_post': hot_post,
    'top_of_the_week': top_of_the_week
  }

  return render(request, template_name, context)

# Blog Page
def BlogHome(request):
  template_name = 'blog.html'
  category = Category.objects.all()

  context = {
    'category': category
  }

  return render(request, template_name, context)

# Blog Details Page
def PostDetails(request, slug):
  template_name = "article.html"
  categories = Category.objects.all()
  post = get_object_or_404(Blog, slug=slug)
  recent_stories = Blog.objects.all().order_by('created_at')[:3]
  popular_posts = Blog.objects.all().order_by('created_at')[3:10]
  form = CommentForm()
  if request.method == "POST":
    form = CommentForm(request.POST or None)
    if form.is_valid():
      c = form.save(commit=False)
      c.post = post
      c.save()

      return redirect('post_details', slug=slug)

  post_comments = Comment.objects.filter(post=post)

  context = {
    'post': post,
    'categories': categories,
    'recent_stories': recent_stories,
    'popular_posts': popular_posts,
    'form': form,
    'post_comments': post_comments,
  }

  return render(request, template_name, context)