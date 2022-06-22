from django.shortcuts import get_object_or_404, redirect, render
from app.forms import CommentForm

from app.models import *

# Create your views here.
# Index (Home) Page
def IndexPage(request):
  template_name = 'index.html'
  featured_posts = Blog.objects.all()[:3]
  recent_posts = Blog.objects.all().order_by('-created_at')[3:7]
  popular_post = Blog.objects.all().order_by('-created_at')[11]
  most_read_posts = Blog.objects.all().order_by('-created_at')[17:21]
  hot_post = Blog.objects.all().order_by('?')[0]
  top_of_the_week = Blog.objects.all().order_by('-created_at')[21:24]

  context = {
    'featured_posts': featured_posts,
    'recent_posts': recent_posts,
    'popular_post': popular_post,
    'most_read_posts': most_read_posts,
    'hot_post': hot_post,
    'top_of_the_week': top_of_the_week
  }

  return render(request, template_name, context)

# Blog Page
def BlogHome(request):
  template_name = 'blog.html'

  return render(request, template_name)

# Blog Details Page
def PostDetails(request, slug):
  template_name = "article.html"
  post = get_object_or_404(Blog, slug=slug)
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
    'form': form,
    'post_comments': post_comments,
  }

  return render(request, template_name, context)